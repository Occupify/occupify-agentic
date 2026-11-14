// Occupify AI Agent Console Client
(function () {
  "use strict";

  // State
  let currentSessionId = null;
  let isStreaming = false;
  let isLogPaused = false;
  let logScope = "session"; // 'all' | 'session'
  let logEntries = [];
  const MAX_LOG_ROWS = 500;
  let eventSource = null;

  // Running token counts for current chat
  let chatTokensIn = 0;
  let chatTokensOut = 0;
  let chatTokensReasoning = 0;

  // DOM Elements
  const userIdInput = document.getElementById("user-id-input");
  const sessionListEl = document.getElementById("session-list");
  const newChatBtn = document.getElementById("new-chat-btn");
  const currentChatTitleEl = document.getElementById("current-chat-title");
  const chatStatusEl = document.getElementById("chat-status");
  const chatMessagesEl = document.getElementById("chat-messages");
  const emptyStateEl = document.getElementById("empty-state");
  const chatFormEl = document.getElementById("chat-form");
  const messageInputEl = document.getElementById("message-input");
  const contextInputEl = document.getElementById("context-input");
  const filesInputEl = document.getElementById("files-input");
  const filesSelectedCountEl = document.getElementById("files-selected-count");
  const sendBtn = document.getElementById("send-btn");
  const stopBtn = document.getElementById("stop-btn");
  const attachBtn = document.getElementById("attach-btn");
  const attachmentsPreviewEl = document.getElementById("attachments-preview");
  const composerBoxEl = document.getElementById("composer-box");
  const formErrorEl = document.getElementById("form-error");

  let currentAbortController = null;
  let selectedFiles = [];

  // Trace & Log Panel Elements
  const togglePanelBtn = document.getElementById("toggle-panel-btn");
  const logPanelEl = document.getElementById("log-panel");
  const tabTraceBtn = document.getElementById("tab-trace-btn");
  const tabRawBtn = document.getElementById("tab-raw-btn");
  const traceViewEl = document.getElementById("trace-view");
  const rawLogViewEl = document.getElementById("raw-log-view");
  const traceFeedEl = document.getElementById("trace-feed");
  const logTableBodyEl = document.getElementById("log-table-body");
  const logFilterAll = document.getElementById("log-filter-all");
  const logFilterSession = document.getElementById("log-filter-session");
  const logPauseBtn = document.getElementById("log-pause-btn");
  const logClearBtn = document.getElementById("log-clear-btn");
  const statTokensInEl = document.getElementById("stat-tokens-in");
  const statTokensOutEl = document.getElementById("stat-tokens-out");
  const statTokensReasoningEl = document.getElementById("stat-tokens-reasoning");
  const statTokensTotalEl = document.getElementById("stat-tokens-total");

  // State & Memory Proof Elements
  const stateStageBadgeEl = document.getElementById("state-stage-badge");
  const stateSeqEl = document.getElementById("state-seq");
  const stateNextActionEl = document.getElementById("state-next-action");
  const stateCompletedStepsEl = document.getElementById("state-completed-steps");
  const stateBlockersEl = document.getElementById("state-blockers");
  const stateMemoryCountEl = document.getElementById("state-memory-count");
  const stateMemoryItemsEl = document.getElementById("state-memory-items");

  async function refreshStateAndMemory(sessionId) {
    const targetSession = sessionId || "new";
    try {
      const res = await fetch(`/ai/dev/state/${targetSession}`, { headers: getHeaders() });
      if (!res.ok) return;
      const json = await res.json();
      const data = json.data || {};
      const cp = data.latest_checkpoint;
      const mem = data.active_user_memory || [];

      if (cp) {
        if (stateStageBadgeEl) stateStageBadgeEl.textContent = cp.stage || "DISCOVERY";
        if (stateSeqEl) stateSeqEl.textContent = `#${cp.checkpoint_seq || 1}`;
        if (stateNextActionEl) stateNextActionEl.textContent = cp.next_action || "None";
        if (stateCompletedStepsEl) stateCompletedStepsEl.textContent = `${(cp.completed_steps || []).length} steps`;
        if (stateBlockersEl) stateBlockersEl.textContent = `${(cp.blockers || []).length}`;
      } else {
        if (stateStageBadgeEl) stateStageBadgeEl.textContent = "DISCOVERY";
        if (stateSeqEl) stateSeqEl.textContent = "#0";
        if (stateNextActionEl) stateNextActionEl.textContent = "Awaiting prompt...";
        if (stateCompletedStepsEl) stateCompletedStepsEl.textContent = "0 steps";
        if (stateBlockersEl) stateBlockersEl.textContent = "0";
      }
      if (stateMemoryCountEl) stateMemoryCountEl.textContent = `${mem.length}`;
      if (stateMemoryItemsEl) {
        if (mem.length === 0) {
          stateMemoryItemsEl.innerHTML = '<span class="empty-hint">No facts stored for this user yet</span>';
        } else {
          stateMemoryItemsEl.innerHTML = "";
          mem.forEach(it => {
            const pill = document.createElement("span");
            pill.className = `memory-pill ${it.is_confirmed ? "confirmed" : "inferred"}`;
            pill.title = `Source: ${it.source} | Confidence: ${it.confidence}`;
            pill.textContent = `[${it.category}] ${it.key}: ${typeof it.value === "object" ? JSON.stringify(it.value) : it.value} (${it.is_confirmed ? "✓" : "?"})`;
            stateMemoryItemsEl.appendChild(pill);
          });
        }
      }
    } catch (_) { }
  }

  function renderStateProofDetails(card, state, memory) {
    if (!state && (!memory || memory.length === 0)) return;
    const details = document.createElement("details");
    details.className = "state-proof-details";

    const stage = state ? state.stage : "DISCOVERY";
    const seq = state ? state.checkpoint_seq : 1;
    const memCount = memory ? memory.length : 0;

    const summary = document.createElement("summary");
    summary.textContent = `🔍 Injected State & Memory Proof (Stage: ${stage} #${seq} | ${memCount} Facts)`;
    details.appendChild(summary);

    const content = document.createElement("div");
    content.className = "state-proof-content";

    if (state) {
      const stateHeader = document.createElement("div");
      stateHeader.className = "state-proof-section-title";
      stateHeader.textContent = `Task Checkpoint (#${state.checkpoint_seq} - ${state.stage})`;
      content.appendChild(stateHeader);

      if (state.goal) {
        const goalDiv = document.createElement("div");
        goalDiv.innerHTML = `<strong>Goal:</strong> ${state.goal}`;
        content.appendChild(goalDiv);
      }
      if (state.completed_steps && state.completed_steps.length > 0) {
        const compDiv = document.createElement("div");
        compDiv.innerHTML = `<strong>Completed:</strong> ${state.completed_steps.join(", ")}`;
        content.appendChild(compDiv);
      }
      if (state.pending_steps && state.pending_steps.length > 0) {
        const pendDiv = document.createElement("div");
        pendDiv.innerHTML = `<strong>Pending:</strong> ${state.pending_steps.join(", ")}`;
        content.appendChild(pendDiv);
      }
      if (state.next_action) {
        const nextDiv = document.createElement("div");
        nextDiv.innerHTML = `<strong>Next Action:</strong> ${state.next_action}`;
        content.appendChild(nextDiv);
      }
    }

    if (memory && memory.length > 0) {
      const memHeader = document.createElement("div");
      memHeader.className = "state-proof-section-title";
      memHeader.style.marginTop = "0.4rem";
      memHeader.textContent = "Active User Memory Injected";
      content.appendChild(memHeader);

      const memList = document.createElement("div");
      memList.style.display = "flex";
      memList.style.flexDirection = "column";
      memList.style.gap = "0.2rem";

      memory.forEach(it => {
        const mRow = document.createElement("div");
        const status = it.is_confirmed ? "<span style='color:#34d399;'>confirmed</span>" : "<span style='color:#fbbf24;'>inferred</span>";
        const valStr = typeof it.value === "object" ? JSON.stringify(it.value) : it.value;
        mRow.innerHTML = `• <code>[${it.category}] ${it.key}</code>: <strong>${valStr}</strong> (${status})`;
        memList.appendChild(mRow);
      });
      content.appendChild(memList);
    }

    details.appendChild(content);
    card.appendChild(details);
  }

  function escapeHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function formatMessageText(str) {
    if (!str) return "";
    let escaped = escapeHtml(str);

    // Bold: **text**
    escaped = escaped.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

    // Markdown links: [Title](URL)
    escaped = escaped.replace(/\[(.*?)\]\((.*?)\)/g, function (match, title, url) {
      const cleanUrl = url.replace(/&amp;/g, "&");
      const isDownload = cleanUrl.includes("/ai/cv-improvement/download/") || cleanUrl.endsWith(".pdf") || cleanUrl.endsWith(".tex");
      if (isDownload) {
        return `<a href="${cleanUrl}" download target="_blank" class="chat-download-btn">📥 ${title}</a>`;
      }
      return `<a href="${cleanUrl}" target="_blank" rel="noopener noreferrer" class="chat-inline-link">${title}</a>`;
    });

    return escaped;
  }

  function renderCvSuggestions(card, bodyText, rawText) {
    if (!rawText || !rawText.includes("<!-- CV_SUGGESTIONS_START")) return;
    if (card.querySelector(".cv-suggestions-container")) return; // Prevent duplicate render

    const match = rawText.match(/<!-- CV_SUGGESTIONS_START\s*([\s\S]*?)\s*CV_SUGGESTIONS_END -->/);
    if (!match) return;

    let payload = null;
    try {
      payload = JSON.parse(match[1]);
    } catch (e) {
      console.error("Failed to parse CV suggestions payload", e);
      return;
    }

    const { sessionId, targetRole, suggestions } = payload;
    if (!sessionId || !suggestions || suggestions.length === 0) return;

    // Clean comment from displayed text
    if (bodyText) {
      const cleanText = rawText.replace(/<!-- CV_SUGGESTIONS_START[\s\S]*?CV_SUGGESTIONS_END -->/, "").trim();
      bodyText.innerHTML = formatMessageText(cleanText);
    }

    const container = document.createElement("div");
    container.className = "cv-suggestions-container";
    container.dataset.sessionId = sessionId;

    const titleEl = document.createElement("div");
    titleEl.className = "cv-suggestions-title";
    titleEl.innerHTML = `<span>🎯 Đề Xuất Cải Thiện CV</span> <span class="badge-role">${escapeHtml(targetRole || "Mục tiêu")}</span>`;
    container.appendChild(titleEl);

    const subhint = document.createElement("div");
    subhint.className = "cv-suggestions-hint";
    subhint.textContent = "Bạn hãy xem xét từng đề xuất bên dưới và đưa ra quyết định duyệt trước khi xuất CV:";
    container.appendChild(subhint);

    const listEl = document.createElement("div");
    listEl.className = "cv-suggestions-list";

    suggestions.forEach((sug, idx) => {
      const sugId = sug.id || `sug-${idx + 1}`;
      const cardEl = document.createElement("div");
      cardEl.className = "suggestion-card";
      cardEl.dataset.suggestionId = sugId;

      const header = document.createElement("div");
      header.className = "suggestion-header";
      header.innerHTML = `<strong>#${escapeHtml(sugId)} [${escapeHtml(sug.section || "Mục CV")}]</strong> <span class="suggestion-status-badge pending">Chờ duyệt</span>`;
      cardEl.appendChild(header);

      const origEl = document.createElement("div");
      origEl.className = "suggestion-orig";
      origEl.innerHTML = `<span class="label">Văn bản gốc:</span> <em>"${escapeHtml(sug.target_original_text || "")}"</em>`;
      cardEl.appendChild(origEl);

      const revEl = document.createElement("div");
      revEl.className = "suggestion-revised";
      revEl.innerHTML = `<span class="label">Đề xuất cải thiện:</span> <strong>"${escapeHtml(sug.suggested_revised_text || "")}"</strong>`;
      cardEl.appendChild(revEl);

      if (sug.reason) {
        const reasonEl = document.createElement("div");
        reasonEl.className = "suggestion-reason";
        reasonEl.innerHTML = `<span class="label">Lý do:</span> ${escapeHtml(sug.reason)}`;
        cardEl.appendChild(reasonEl);
      }

      // Inline edit box
      const editBox = document.createElement("div");
      editBox.className = "suggestion-edit-box";
      editBox.style.display = "none";
      const editArea = document.createElement("textarea");
      editArea.className = "suggestion-edit-textarea";
      editArea.rows = 2;
      editArea.value = sug.suggested_revised_text || "";
      const saveEditBtn = document.createElement("button");
      saveEditBtn.className = "btn btn-sm btn-primary";
      saveEditBtn.textContent = "Lưu sửa đổi";
      editBox.appendChild(editArea);
      editBox.appendChild(saveEditBtn);
      cardEl.appendChild(editBox);

      // Actions row
      const actions = document.createElement("div");
      actions.className = "suggestion-actions";

      const approveBtn = document.createElement("button");
      approveBtn.type = "button";
      approveBtn.className = "btn btn-sm btn-outline-success btn-approve";
      approveBtn.textContent = "✓ Chấp thuận";

      const rejectBtn = document.createElement("button");
      rejectBtn.type = "button";
      rejectBtn.className = "btn btn-sm btn-outline-danger btn-reject";
      rejectBtn.textContent = "✕ Từ chối";

      const editBtn = document.createElement("button");
      editBtn.type = "button";
      editBtn.className = "btn btn-sm btn-outline btn-edit";
      editBtn.textContent = "Chỉnh sửa";

      actions.appendChild(approveBtn);
      actions.appendChild(rejectBtn);
      actions.appendChild(editBtn);
      cardEl.appendChild(actions);

      const statusBadge = header.querySelector(".suggestion-status-badge");

      approveBtn.addEventListener("click", async () => {
        approveBtn.disabled = true;
        try {
          const res = await fetch(`/ai/cv-improvement/${sessionId}/decide`, {
            method: "POST",
            headers: { ...getHeaders(), "Content-Type": "application/json" },
            body: JSON.stringify({ suggestion_id: sugId, decision: "APPROVED" })
          });
          if (res.ok) {
            statusBadge.textContent = "✓ Đã duyệt";
            statusBadge.className = "suggestion-status-badge approved";
            editBox.style.display = "none";
          }
        } catch (e) {
          console.error("Failed to approve suggestion", e);
        } finally {
          approveBtn.disabled = false;
        }
      });

      rejectBtn.addEventListener("click", async () => {
        rejectBtn.disabled = true;
        try {
          const res = await fetch(`/ai/cv-improvement/${sessionId}/decide`, {
            method: "POST",
            headers: { ...getHeaders(), "Content-Type": "application/json" },
            body: JSON.stringify({ suggestion_id: sugId, decision: "REJECTED" })
          });
          if (res.ok) {
            statusBadge.textContent = "✕ Đã từ chối";
            statusBadge.className = "suggestion-status-badge rejected";
            editBox.style.display = "none";
          }
        } catch (e) {
          console.error("Failed to reject suggestion", e);
        } finally {
          rejectBtn.disabled = false;
        }
      });

      editBtn.addEventListener("click", () => {
        editBox.style.display = editBox.style.display === "none" ? "block" : "none";
        if (editBox.style.display === "block") {
          editArea.focus();
        }
      });

      saveEditBtn.addEventListener("click", async () => {
        const newText = editArea.value.trim();
        if (!newText) return;
        saveEditBtn.disabled = true;
        try {
          const res = await fetch(`/ai/cv-improvement/${sessionId}/decide`, {
            method: "POST",
            headers: { ...getHeaders(), "Content-Type": "application/json" },
            body: JSON.stringify({ suggestion_id: sugId, decision: "EDITED", user_text: newText })
          });
          if (res.ok) {
            statusBadge.textContent = "✎ Đã sửa";
            statusBadge.className = "suggestion-status-badge edited";
            revEl.querySelector("strong").textContent = `"${newText}"`;
            editBox.style.display = "none";
          }
        } catch (e) {
          console.error("Failed to save edited suggestion", e);
        } finally {
          saveEditBtn.disabled = false;
        }
      });

      listEl.appendChild(cardEl);
    });

    container.appendChild(listEl);

    // Bottom action bar
    const footerBar = document.createElement("div");
    footerBar.className = "cv-suggestions-footer";

    const finalizeBtn = document.createElement("button");
    finalizeBtn.type = "button";
    finalizeBtn.className = "btn btn-primary btn-finalize-cv";
    finalizeBtn.innerHTML = "Xuất File PDF";

    const downloadContainer = document.createElement("div");
    downloadContainer.className = "cv-download-result";
    downloadContainer.style.display = "none";

    finalizeBtn.addEventListener("click", async () => {
      finalizeBtn.disabled = true;
      finalizeBtn.textContent = "Đang tạo file PDF & tải lên...";
      try {
        const res = await fetch(`/ai/cv-improvement/${sessionId}/generate`, {
          method: "POST",
          headers: getHeaders(),
        });
        const json = await res.json();
        if (res.ok && json.data && json.data.pdf_url) {
          const pdfUrl = json.data.pdf_url;
          downloadContainer.style.display = "block";
          downloadContainer.innerHTML = `
            <div style="background-color: #064e3b; border: 1px solid #059669; border-radius: 4px; padding: 0.6rem; color: #a7f3d0; margin-top: 0.4rem;">
              <strong>Xuất CV thành công!</strong><br/>
              <a href="${pdfUrl}" target="_blank" class="btn btn-sm btn-outline-success" style="margin-top:0.4rem; display:inline-block; text-decoration:none; font-weight:600;">📥 Tải File PDF CV</a>
            </div>
          `;
          finalizeBtn.style.display = "none";
        } else {
          const errMsg = (json && json.message) || "Không thể tạo file PDF.";
          alert(`Lỗi xuất CV: ${errMsg}`);
          finalizeBtn.textContent = "Thử Xuất PDF Lại";
          finalizeBtn.disabled = false;
        }
      } catch (e) {
        console.error("Failed to generate CV", e);
        alert("Đã xảy ra lỗi khi kết nối tới máy chủ.");
        finalizeBtn.textContent = "Thử Xuất PDF Lại";
        finalizeBtn.disabled = false;
      }
    });

    footerBar.appendChild(finalizeBtn);
    footerBar.appendChild(downloadContainer);
    container.appendChild(footerBar);

    card.appendChild(container);
  }


  // User ID setup
  function getUserId() {
    return userIdInput.value.trim() || "dev-user-1";
  }

  function initUserId() {
    const saved = localStorage.getItem("occupify_user_id");
    userIdInput.value = saved || "dev-user-1";
    userIdInput.addEventListener("change", function () {
      const val = userIdInput.value.trim() || "dev-user-1";
      localStorage.setItem("occupify_user_id", val);
      currentSessionId = null;
      loadSessions();
      refreshStateAndMemory(null);
    });
  }

  // File selection & preview
  function updateFilesPreview() {
    if (!attachmentsPreviewEl) return;
    attachmentsPreviewEl.innerHTML = "";
    if (selectedFiles.length === 0) {
      attachmentsPreviewEl.style.display = "none";
      if (filesSelectedCountEl) filesSelectedCountEl.textContent = "";
      return;
    }
    attachmentsPreviewEl.style.display = "flex";
    if (filesSelectedCountEl) {
      filesSelectedCountEl.textContent = `${selectedFiles.length}/3`;
    }

    selectedFiles.forEach((file, index) => {
      const chip = document.createElement("div");
      chip.className = "file-preview-chip";

      const nameSpan = document.createElement("span");
      nameSpan.className = "file-chip-name";
      nameSpan.title = file.name;
      nameSpan.textContent = `📄 ${file.name}`;

      const removeBtn = document.createElement("button");
      removeBtn.type = "button";
      removeBtn.className = "file-chip-remove";
      removeBtn.title = "Bỏ file này";
      removeBtn.innerHTML = "&times;";
      removeBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        selectedFiles.splice(index, 1);
        updateFilesPreview();
      });

      chip.appendChild(nameSpan);
      chip.appendChild(removeBtn);
      attachmentsPreviewEl.appendChild(chip);
    });
  }

  if (attachBtn) {
    attachBtn.addEventListener("click", () => {
      filesInputEl.click();
    });
  }

  filesInputEl.addEventListener("change", function () {
    const newFiles = Array.from(filesInputEl.files);
    for (const f of newFiles) {
      if (selectedFiles.length >= 3) {
        showError("Chỉ được đính kèm tối đa 3 file PDF.");
        break;
      }
      if (!selectedFiles.some((existing) => existing.name === f.name && existing.size === f.size)) {
        selectedFiles.push(f);
      }
    }
    filesInputEl.value = "";
    updateFilesPreview();
  });

  // Drag & drop files onto composer box
  if (composerBoxEl) {
    composerBoxEl.addEventListener("dragover", (e) => {
      e.preventDefault();
      composerBoxEl.classList.add("drag-over");
    });
    composerBoxEl.addEventListener("dragleave", () => {
      composerBoxEl.classList.remove("drag-over");
    });
    composerBoxEl.addEventListener("drop", (e) => {
      e.preventDefault();
      composerBoxEl.classList.remove("drag-over");
      if (e.dataTransfer && e.dataTransfer.files) {
        const dropped = Array.from(e.dataTransfer.files).filter((f) =>
          f.name.toLowerCase().endsWith(".pdf")
        );
        if (dropped.length === 0) {
          showError("Chỉ chấp nhận file định dạng PDF.");
          return;
        }
        for (const f of dropped) {
          if (selectedFiles.length >= 3) {
            showError("Chỉ được đính kèm tối đa 3 file PDF.");
            break;
          }
          if (!selectedFiles.some((existing) => existing.name === f.name && existing.size === f.size)) {
            selectedFiles.push(f);
          }
        }
        updateFilesPreview();
      }
    });
  }

  // Auto-resize textarea
  function autoResizeTextarea() {
    messageInputEl.style.height = "auto";
    messageInputEl.style.height = Math.min(messageInputEl.scrollHeight, 180) + "px";
  }
  messageInputEl.addEventListener("input", autoResizeTextarea);

  // Stop button listener
  if (stopBtn) {
    stopBtn.addEventListener("click", function () {
      if (currentAbortController) {
        currentAbortController.abort();
        chatStatusEl.textContent = "Đã dừng";
        chatStatusEl.className = "chat-status-badge interrupted";
      }
    });
  }

  // Enter to send in textarea
  messageInputEl.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (!isStreaming && messageInputEl.value.trim()) {
        chatFormEl.dispatchEvent(new Event("submit", { cancelable: true }));
      }
    }
  });

  // API Call helpers
  function getHeaders() {
    return {
      "x-user-id": getUserId(),
      "x-user-role": "ROLE_USER",
    };
  }

  // Load Sessions List
  async function loadSessions() {
    try {
      const res = await fetch("/ai/chat/sessions?limit=50", {
        headers: getHeaders(),
      });
      if (!res.ok) return;
      const data = await res.json();
      const sessions = data.data || [];
      renderSessionList(sessions);
      if (!currentSessionId && sessions.length > 0) {
        selectSession(sessions[0].id, sessions[0].title);
      } else if (!currentSessionId) {
        refreshStateAndMemory(null);
      }
    } catch (err) {
      console.error("Failed to load sessions:", err);
    }
  }

  function renderSessionList(sessions) {
    sessionListEl.textContent = "";
    if (sessions.length === 0) {
      const emptyDiv = document.createElement("div");
      emptyDiv.className = "session-meta";
      emptyDiv.style.padding = "0.75rem";
      emptyDiv.textContent = "No saved chats";
      sessionListEl.appendChild(emptyDiv);
      return;
    }

    sessions.forEach((s) => {
      const item = document.createElement("div");
      item.className = "session-item" + (s.id === currentSessionId ? " active" : "");
      item.dataset.sessionId = s.id;

      const info = document.createElement("div");
      info.className = "session-info";

      const title = document.createElement("span");
      title.className = "session-title";
      title.textContent = s.title || "Untitled Chat";

      const meta = document.createElement("span");
      meta.className = "session-meta";
      const dt = new Date(s.updatedAt || s.createdAt);
      meta.textContent = dt.toLocaleDateString() + " " + dt.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

      info.appendChild(title);
      info.appendChild(meta);

      const delBtn = document.createElement("button");
      delBtn.className = "session-delete-btn";
      delBtn.title = "Delete session";
      delBtn.textContent = "✕";
      delBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        deleteSession(s.id);
      });

      item.appendChild(info);
      item.appendChild(delBtn);

      item.addEventListener("click", function () {
        selectSession(s.id, s.title);
      });

      sessionListEl.appendChild(item);
    });
  }

  async function selectSession(sessionId, title) {
    if (isStreaming) return;
    currentSessionId = sessionId;
    currentChatTitleEl.textContent = title || "Conversation";
    resetTokenStats();
    refreshStateAndMemory(sessionId);

    // Update active highlight
    const items = sessionListEl.querySelectorAll(".session-item");
    items.forEach((it) => {
      if (it.dataset.sessionId === sessionId) {
        it.classList.add("active");
      } else {
        it.classList.remove("active");
      }
    });

    // Re-filter logs and traces if in session scope
    renderAllLogsAndTraces();

    // Fetch messages
    try {
      chatMessagesEl.textContent = "";
      const res = await fetch(`/ai/chat/sessions/${sessionId}/messages?limit=100`, {
        headers: getHeaders(),
      });
      if (!res.ok) return;
      const data = await res.json();
      const messages = data.data || [];
      if (messages.length === 0) {
        chatMessagesEl.appendChild(emptyStateEl);
      } else {
        messages.forEach((m) => {
          appendMessageCard(m.role, m.displayText || m.content || "", m.status, m.model, m.tokensIn, m.tokensOut, m.attachments);
        });
      }
      chatMessagesEl.scrollTop = chatMessagesEl.scrollHeight;
    } catch (err) {
      console.error("Failed to load session messages:", err);
    }
  }

  async function deleteSession(sessionId) {
    if (!confirm("Delete this chat?")) return;
    try {
      const res = await fetch(`/ai/chat/sessions/${sessionId}`, {
        method: "DELETE",
        headers: getHeaders(),
      });
      if (!res.ok) {
        showError("Failed to delete session.");
        return;
      }
      if (currentSessionId === sessionId) {
        startNewChat();
      }
      await loadSessions();
    } catch (err) {
      console.error("Failed to delete session:", err);
      showError("Failed to delete session.");
    }
  }

  function startNewChat() {
    if (isStreaming) return;
    currentSessionId = null;
    currentChatTitleEl.textContent = "New Conversation";
    chatMessagesEl.textContent = "";
    chatMessagesEl.appendChild(emptyStateEl);
    resetTokenStats();
    refreshStateAndMemory(null);

    const items = sessionListEl.querySelectorAll(".session-item");
    items.forEach((it) => it.classList.remove("active"));
    renderAllLogsAndTraces();
    messageInputEl.focus();
  }

  newChatBtn.addEventListener("click", startNewChat);

  // Render Attachment Summary with textContent (F-02)
  function renderAttachments(card, attachments) {
    if (!attachments || !attachments.length) return;
    let container = card.querySelector(".message-attachments");
    if (!container) {
      container = document.createElement("div");
      container.className = "message-attachments";
      card.appendChild(container);
    }
    container.textContent = "";
    attachments.forEach((att) => {
      const item = document.createElement("div");
      item.className = "attachment-item";
      const fileName = att.fileName || att.file_name || "Attachment";
      const pages = att.pages ?? 0;
      let removedDesc = "none";
      if (att.removed && typeof att.removed === "object") {
        const parts = Object.entries(att.removed)
          .filter(([_, count]) => count > 0)
          .map(([type, count]) => `${type}: ${count}`);
        if (parts.length > 0) {
          removedDesc = parts.join(", ");
        }
      }
      item.textContent = `📎 ${fileName} (${pages} page${pages === 1 ? "" : "s"}, removed: ${removedDesc})`;
      container.appendChild(item);
    });
  }

  // Append Message Card to UI
  function appendMessageCard(role, text, status, model, tokensIn, tokensOut, attachments) {
    if (emptyStateEl.parentNode === chatMessagesEl) {
      chatMessagesEl.removeChild(emptyStateEl);
    }

    const card = document.createElement("div");
    card.className = `message-card message-${role}`;
    if (status === "interrupted") {
      card.classList.add("interrupted");
    }

    const tag = document.createElement("div");
    tag.className = "message-tag";
    tag.textContent = role === "user" ? "You" : (status === "interrupted" ? "Assistant (interrupted)" : "Assistant");
    card.appendChild(tag);

    const bodyText = document.createElement("div");
    bodyText.className = "message-body";
    if (role === "assistant") {
      bodyText.innerHTML = formatMessageText(text);
    } else {
      bodyText.textContent = text;
    }
    card.appendChild(bodyText);

    if (role === "assistant" && (model || tokensIn || tokensOut)) {
      const footer = document.createElement("div");
      footer.className = "message-meta-footer";
      if (model) {
        const mSpan = document.createElement("span");
        mSpan.textContent = `Model: ${model}`;
        footer.appendChild(mSpan);
      }
      if (tokensIn || tokensOut) {
        const uSpan = document.createElement("span");
        uSpan.textContent = `Tokens: ${tokensIn || 0} in / ${tokensOut || 0} out`;
        footer.appendChild(uSpan);
      }
      card.appendChild(footer);
    }

    if (attachments && attachments.length > 0) {
      renderAttachments(card, attachments);
    }

    if (role === "assistant" && text) {
      renderCvSuggestions(card, bodyText, text);
    }

    chatMessagesEl.appendChild(card);
    chatMessagesEl.scrollTop = chatMessagesEl.scrollHeight;
    return { card, bodyText };
  }

  // Chat Form Submit (Streaming Send)
  chatFormEl.addEventListener("submit", async function (e) {
    e.preventDefault();
    if (isStreaming) return;

    const messageText = messageInputEl.value.trim();
    if (!messageText) return;

    const contextText = contextInputEl.value.trim();

    if (selectedFiles.length > 3) {
      showError("Chỉ được đính kèm tối đa 3 file PDF.");
      return;
    }

    clearError();
    isStreaming = true;
    currentAbortController = new AbortController();
    sendBtn.style.display = "none";
    if (stopBtn) stopBtn.style.display = "inline-flex";
    chatStatusEl.textContent = "Streaming...";
    chatStatusEl.className = "chat-status-badge streaming";

    // 1. Append user bubble
    const userElements = appendMessageCard("user", messageText);
    messageInputEl.value = "";
    messageInputEl.style.height = "auto";

    // 2. Prepare assistant bubble with live streaming cursor
    const asstElements = appendMessageCard("assistant", "");
    const cursor = document.createElement("span");
    cursor.className = "typing-cursor";
    asstElements.bodyText.appendChild(cursor);

    // Build FormData
    const formData = new FormData();
    formData.append("message", messageText);
    if (currentSessionId) {
      formData.append("sessionId", currentSessionId);
    }
    if (contextText) {
      formData.append("context", contextText);
    }
    for (let i = 0; i < selectedFiles.length; i++) {
      formData.append("files", selectedFiles[i]);
    }

    let fullReply = "";
    let responseModel = "";
    let finalUsage = null;
    let lastDoneState = null;
    let lastDoneMemory = null;

    try {
      const res = await fetch("/ai/chat/messages?stream=true", {
        method: "POST",
        headers: getHeaders(),
        body: formData,
        signal: currentAbortController.signal,
      });

      if (!res.ok) {
        let errJson = null;
        try {
          errJson = await res.json();
        } catch (_) { }
        const errMsg = (errJson && errJson.message) || `Request failed with status ${res.status}`;
        throw new Error(errMsg);
      }

      // Read SSE stream
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const blocks = buffer.split("\n\n");
        buffer = blocks.pop(); // keep partial chunk

        for (const block of blocks) {
          if (!block.trim()) continue;
          const lines = block.split("\n");
          let eventName = "";
          let dataStr = "";

          for (const line of lines) {
            if (line.startsWith(":")) {
              // Ignore SSE comments/pings
              continue;
            }
            if (line.startsWith("event:")) {
              eventName = line.substring(6).trim();
            } else if (line.startsWith("data:")) {
              dataStr = line.substring(5).trim();
            }
          }

          if (eventName === "meta" && dataStr) {
            try {
              const meta = JSON.parse(dataStr);
              if (meta.sessionId && !currentSessionId) {
                currentSessionId = meta.sessionId;
                currentChatTitleEl.textContent = messageText.slice(0, 40);
                loadSessions();
              }
              if (meta.attachments && meta.attachments.length > 0) {
                renderAttachments(userElements.card, meta.attachments);
              }
            } catch (_) { }
          } else if (eventName === "delta" && dataStr) {
            try {
              const delta = JSON.parse(dataStr);
              if (delta.text) {
                fullReply += delta.text;
                asstElements.bodyText.textContent = fullReply;
                asstElements.bodyText.appendChild(cursor);
                chatMessagesEl.scrollTop = chatMessagesEl.scrollHeight;
              }
            } catch (_) { }
          } else if (eventName === "done" && dataStr) {
            try {
              const doneData = JSON.parse(dataStr);
              responseModel = doneData.model || "";
              finalUsage = doneData.usage || null;
              lastDoneState = doneData.state || null;
              lastDoneMemory = doneData.memory || null;
            } catch (_) { }
          } else if (eventName === "error" && dataStr) {
            try {
              const errPayload = JSON.parse(dataStr);
              const errMsg = errPayload.message || "Failed to generate reply.";
              showError(errMsg);
              fullReply += `\n[${errMsg}]`;
              asstElements.bodyText.innerHTML = formatMessageText(fullReply);
            } catch (_) { }
          }
        }
      }

      // Stream completed
      if (cursor.parentNode) {
        cursor.parentNode.removeChild(cursor);
      }
      asstElements.bodyText.innerHTML = formatMessageText(fullReply);

      if (responseModel || finalUsage) {
        const footer = document.createElement("div");
        footer.className = "message-meta-footer";
        if (responseModel) {
          const mSpan = document.createElement("span");
          mSpan.textContent = `Model: ${responseModel}`;
          footer.appendChild(mSpan);
        }
        if (finalUsage) {
          const uSpan = document.createElement("span");
          uSpan.textContent = `Tokens: ${finalUsage.tokensIn || 0} in / ${finalUsage.tokensOut || 0} out`;
          footer.appendChild(uSpan);
        }
        asstElements.card.appendChild(footer);
      }

      // Render In-Message State & Memory Proof (K4)
      if (lastDoneState || (lastDoneMemory && lastDoneMemory.length > 0)) {
        renderStateProofDetails(asstElements.card, lastDoneState, lastDoneMemory);
      }
      renderCvSuggestions(asstElements.card, asstElements.bodyText, fullReply);
      if (currentSessionId) {
        refreshStateAndMemory(currentSessionId);
      }

      // Clear file selection
      selectedFiles = [];
      updateFilesPreview();
      loadSessions();

    } catch (err) {
      if (cursor.parentNode) {
        cursor.parentNode.removeChild(cursor);
      }
      if (err.name === "AbortError") {
        fullReply += (fullReply ? "\n\n" : "") + "*⏹ Phản hồi đã được dừng bởi người dùng.*";
        asstElements.bodyText.textContent = fullReply;
        asstElements.card.classList.add("interrupted");
      } else {
        const msg = err.message || "Failed to send message.";
        showError(msg);
        asstElements.bodyText.textContent = fullReply ? (fullReply + `\n[${msg}]`) : `[${msg}]`;
        asstElements.card.classList.add("interrupted");
      }
    } finally {
      isStreaming = false;
      currentAbortController = null;
      sendBtn.style.display = "inline-flex";
      sendBtn.disabled = false;
      if (stopBtn) stopBtn.style.display = "none";
      if (chatStatusEl.textContent !== "Đã dừng") {
        chatStatusEl.textContent = "Ready";
        chatStatusEl.className = "chat-status-badge";
      }
      messageInputEl.focus();
    }
  });

  function showError(msg) {
    formErrorEl.textContent = msg;
    formErrorEl.style.display = "block";
  }

  function clearError() {
    formErrorEl.textContent = "";
    formErrorEl.style.display = "none";
  }

  // --- Live Trace & Log Panel ---
  function initLogs() {
    // Initial fetch of recent 200 logs
    fetchRecentLogs();

    // Listen to live stream
    setupLogEventSource();

    // Panel collapse toggle
    if (togglePanelBtn && logPanelEl) {
      togglePanelBtn.addEventListener("click", function () {
        const isCollapsed = logPanelEl.classList.toggle("collapsed");
        togglePanelBtn.classList.toggle("active", !isCollapsed);
        togglePanelBtn.setAttribute("aria-pressed", (!isCollapsed).toString());
      });
    }

    // View tab switching
    if (tabTraceBtn && tabRawBtn && traceViewEl && rawLogViewEl) {
      tabTraceBtn.addEventListener("click", function () {
        tabTraceBtn.classList.add("active");
        tabTraceBtn.setAttribute("aria-selected", "true");
        tabRawBtn.classList.remove("active");
        tabRawBtn.setAttribute("aria-selected", "false");
        traceViewEl.style.display = "block";
        rawLogViewEl.style.display = "none";
      });

      tabRawBtn.addEventListener("click", function () {
        tabRawBtn.classList.add("active");
        tabRawBtn.setAttribute("aria-selected", "true");
        tabTraceBtn.classList.remove("active");
        tabTraceBtn.setAttribute("aria-selected", "false");
        traceViewEl.style.display = "none";
        rawLogViewEl.style.display = "block";
      });
    }

    // Filter controls
    logFilterAll.addEventListener("change", function () {
      if (logFilterAll.checked) {
        logScope = "all";
        renderAllLogsAndTraces();
      }
    });

    logFilterSession.addEventListener("change", function () {
      if (logFilterSession.checked) {
        logScope = "session";
        renderAllLogsAndTraces();
      }
    });

    // Pause toggle
    logPauseBtn.addEventListener("click", function () {
      isLogPaused = !isLogPaused;
      logPauseBtn.textContent = isLogPaused ? "Resume" : "Pause";
      logPauseBtn.classList.toggle("btn-primary", isLogPaused);
      if (!isLogPaused) {
        renderAllLogsAndTraces();
      }
    });

    // Clear logs and traces
    logClearBtn.addEventListener("click", function () {
      logEntries = [];
      resetTokenStats();
      renderAllLogsAndTraces();
    });
  }

  async function fetchRecentLogs() {
    try {
      const res = await fetch("/ai/dev/logs?limit=200");
      if (!res.ok) return;
      const json = await res.json();
      const entries = json.data || [];
      entries.forEach((e) => pushLogEntry(e, false));
      renderAllLogsAndTraces();
    } catch (err) {
      console.error("Failed to fetch initial logs:", err);
    }
  }

  function setupLogEventSource() {
    if (eventSource) {
      eventSource.close();
    }

    eventSource = new EventSource("/ai/dev/logs/stream");

    eventSource.addEventListener("log", function (evt) {
      if (!evt.data) return;
      try {
        const entry = JSON.parse(evt.data);
        pushLogEntry(entry, true);
      } catch (_) { }
    });

    eventSource.onerror = function () {
      // EventSource reconnects automatically
    };
  }

  function pushLogEntry(entry, shouldUpdateUI) {
    logEntries.push(entry);
    if (logEntries.length > MAX_LOG_ROWS) {
      logEntries.shift();
    }

    // Accumulate tokens for current chat if run.end
    accumulateTokens(entry);

    if (shouldUpdateUI && !isLogPaused) {
      const matchesScope = logScope === "all" || (currentSessionId && entry.session_id === currentSessionId);
      if (matchesScope) {
        appendLogRowToTable(entry);
        if (isHighSignalTraceEvent(entry)) {
          appendTraceStep(entry);
        }
      }
    }
  }

  function accumulateTokens(entry) {
    if (currentSessionId && entry.session_id === currentSessionId) {
      if (entry.event === "run.end") {
        if (typeof entry.tokens_in === "number") chatTokensIn += entry.tokens_in;
        if (typeof entry.tokens_out === "number") chatTokensOut += entry.tokens_out;
        if (typeof entry.tokens_reasoning === "number") chatTokensReasoning += entry.tokens_reasoning;
        updateTokenStatsDisplay();
      }
    }
  }

  function resetTokenStats() {
    chatTokensIn = 0;
    chatTokensOut = 0;
    chatTokensReasoning = 0;
    // Recompute from current log entries
    if (currentSessionId) {
      logEntries.forEach((e) => {
        if (e.session_id === currentSessionId && e.event === "run.end") {
          if (typeof e.tokens_in === "number") chatTokensIn += e.tokens_in;
          if (typeof e.tokens_out === "number") chatTokensOut += e.tokens_out;
          if (typeof e.tokens_reasoning === "number") chatTokensReasoning += e.tokens_reasoning;
        }
      });
    }
    updateTokenStatsDisplay();
  }

  function updateTokenStatsDisplay() {
    statTokensInEl.textContent = chatTokensIn;
    statTokensOutEl.textContent = chatTokensOut;
    statTokensReasoningEl.textContent = chatTokensReasoning;
    statTokensTotalEl.textContent = chatTokensIn + chatTokensOut;
  }

  // --- High-Signal Activity Trace ---
  function isHighSignalTraceEvent(entry) {
    if (!entry || !entry.event) return false;
    if (entry.level === "WARNING" || entry.level === "ERROR") return true;
    const ev = entry.event;
    if (
      ev.startsWith("run.") ||
      ev.startsWith("llm.") ||
      ev.startsWith("state.") ||
      ev.startsWith("memory.") ||
      ev.startsWith("job_match.") ||
      ev.startsWith("tool.")
    ) {
      return true;
    }
    return false;
  }

  function createTraceStepElement(entry) {
    const el = document.createElement("div");
    el.className = "trace-step";

    let badgeText = "EVENT";
    let titleText = entry.event || "action";
    let subText = "";

    const tsStr = entry.ts || "";
    let timeFormatted = "";
    if (tsStr) {
      const d = new Date(tsStr);
      timeFormatted = d.toTimeString().split(" ")[0];
    }

    const ev = entry.event || "";
    if (ev === "run.start") {
      badgeText = "RUN";
      titleText = "Turn started";
      if (entry.model) subText = `Model: ${entry.model}`;
    } else if (ev === "run.end") {
      badgeText = "DONE";
      titleText = `Turn completed${entry.ms ? ` (${entry.ms}ms)` : ""}`;
      subText = `Tokens: ${entry.tokens_in ?? 0} in / ${entry.tokens_out ?? 0} out`;
    } else if (ev === "llm.request") {
      badgeText = "LLM";
      titleText = `Prompt sent to ${entry.model || "model"}`;
    } else if (ev === "llm.response") {
      badgeText = "LLM";
      titleText = "LLM response received";
      subText = `${entry.tokens_out ?? 0} tokens${entry.ms ? ` · ${entry.ms}ms` : ""}`;
    } else if (ev.startsWith("state.")) {
      badgeText = "STATE";
      titleText = `State: ${ev.replace("state.", "").replace("_", " ")}`;
    } else if (ev.startsWith("memory.")) {
      badgeText = "MEMORY";
      titleText = ev === "memory.recorded" ? "Recorded new user memory" : "Loaded active memory";
    } else if (ev.startsWith("job_match.") || ev.startsWith("tool.")) {
      badgeText = "TOOL";
      titleText = `Tool: ${ev}`;
      if (entry.ms) subText = `${entry.ms}ms`;
    } else {
      badgeText = (entry.level || "INFO").toUpperCase();
      titleText = ev;
      if (entry.ms) subText = `${entry.ms}ms`;
    }

    const top = document.createElement("div");
    top.className = "trace-step-top";

    const badge = document.createElement("span");
    badge.className = "trace-badge";
    badge.textContent = badgeText;
    top.appendChild(badge);

    const time = document.createElement("span");
    time.className = "trace-time";
    time.textContent = timeFormatted;
    top.appendChild(time);

    el.appendChild(top);

    const text = document.createElement("div");
    text.className = "trace-text";
    text.textContent = titleText;
    el.appendChild(text);

    if (subText) {
      const sub = document.createElement("div");
      sub.className = "trace-subtext";
      sub.textContent = subText;
      el.appendChild(sub);
    }

    return el;
  }

  function appendTraceStep(entry) {
    if (!traceFeedEl) return;
    const emptyHint = traceFeedEl.querySelector(".trace-empty");
    if (emptyHint) {
      traceFeedEl.removeChild(emptyHint);
    }

    const stepEl = createTraceStepElement(entry);
    traceFeedEl.appendChild(stepEl);

    while (traceFeedEl.children.length > 200) {
      traceFeedEl.removeChild(traceFeedEl.firstChild);
    }

    const container = traceFeedEl.parentElement;
    if (container) {
      container.scrollTop = container.scrollHeight;
    }
  }

  function renderTraces() {
    if (!traceFeedEl) return;
    traceFeedEl.textContent = "";

    const filtered = logEntries.filter((e) => {
      if (!isHighSignalTraceEvent(e)) return false;
      if (logScope === "session") {
        return currentSessionId && e.session_id === currentSessionId;
      }
      return true;
    });

    if (filtered.length === 0) {
      const empty = document.createElement("div");
      empty.className = "trace-empty";
      empty.textContent = "No activity recorded yet";
      traceFeedEl.appendChild(empty);
      return;
    }

    filtered.forEach((e) => {
      traceFeedEl.appendChild(createTraceStepElement(e));
    });

    const container = traceFeedEl.parentElement;
    if (container) {
      container.scrollTop = container.scrollHeight;
    }
  }

  function renderLogs() {
    logTableBodyEl.textContent = "";
    const filtered = logEntries.filter((e) => {
      if (logScope === "session") {
        return currentSessionId && e.session_id === currentSessionId;
      }
      return true;
    });

    filtered.forEach((e) => appendLogRowToTable(e));
  }

  function renderAllLogsAndTraces() {
    renderLogs();
    renderTraces();
  }

  function appendLogRowToTable(entry) {
    const tr = document.createElement("tr");

    // 1. Time (HH:MM:SS)
    const tdTime = document.createElement("td");
    const tsStr = entry.ts || "";
    let timeFormatted = "";
    if (tsStr) {
      const d = new Date(tsStr);
      timeFormatted = d.toTimeString().split(" ")[0];
    }
    tdTime.textContent = timeFormatted;
    tr.appendChild(tdTime);

    // 2. Level Badge
    const tdLevel = document.createElement("td");
    const badge = document.createElement("span");
    const lvl = (entry.level || "INFO").toUpperCase();
    badge.className = `badge-level badge-${lvl.toLowerCase()}`;
    badge.textContent = lvl;
    tdLevel.appendChild(badge);
    tr.appendChild(tdLevel);

    // 3. Event
    const tdEvent = document.createElement("td");
    tdEvent.className = "event-name";
    tdEvent.textContent = entry.event || "log";
    tr.appendChild(tdEvent);

    // 4. Tokens (In/Out)
    const tdTokens = document.createElement("td");
    if (typeof entry.tokens_in === "number" || typeof entry.tokens_out === "number") {
      tdTokens.textContent = `${entry.tokens_in ?? 0}/${entry.tokens_out ?? 0}`;
    } else {
      tdTokens.className = "text-muted";
      tdTokens.textContent = "-";
    }
    tr.appendChild(tdTokens);

    // 5. Latency ms
    const tdLatency = document.createElement("td");
    if (typeof entry.ms === "number") {
      tdLatency.textContent = `${entry.ms}`;
    } else {
      tdLatency.className = "text-muted";
      tdLatency.textContent = "-";
    }
    tr.appendChild(tdLatency);

    logTableBodyEl.appendChild(tr);

    const container = logTableBodyEl.parentElement.parentElement;
    if (container) {
      container.scrollTop = container.scrollHeight;
    }
  }

  // Initialization
  initUserId();
  loadSessions();
  initLogs();
})();
