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
  const formErrorEl = document.getElementById("form-error");

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
    } catch (_) {}
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

  // File selection indicator
  filesInputEl.addEventListener("change", function () {
    const count = filesInputEl.files.length;
    if (count > 0) {
      filesSelectedCountEl.textContent = `${count} PDF${count > 1 ? "s" : ""} selected`;
    } else {
      filesSelectedCountEl.textContent = "";
    }
  });

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
    bodyText.textContent = text;
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
    const files = filesInputEl.files;

    if (files.length > 3) {
      showError("Maximum 3 PDF attachments allowed.");
      return;
    }

    clearError();
    isStreaming = true;
    sendBtn.disabled = true;
    chatStatusEl.textContent = "Streaming...";
    chatStatusEl.className = "chat-status-badge streaming";

    // 1. Append user bubble
    const userElements = appendMessageCard("user", messageText);
    messageInputEl.value = "";

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
    for (let i = 0; i < files.length; i++) {
      formData.append("files", files[i]);
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
      });

      if (!res.ok) {
        let errJson = null;
        try {
          errJson = await res.json();
        } catch (_) {}
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
            } catch (_) {}
          } else if (eventName === "delta" && dataStr) {
            try {
              const delta = JSON.parse(dataStr);
              if (delta.text) {
                fullReply += delta.text;
                asstElements.bodyText.textContent = fullReply;
                asstElements.bodyText.appendChild(cursor);
                chatMessagesEl.scrollTop = chatMessagesEl.scrollHeight;
              }
            } catch (_) {}
          } else if (eventName === "done" && dataStr) {
            try {
              const doneData = JSON.parse(dataStr);
              responseModel = doneData.model || "";
              finalUsage = doneData.usage || null;
              lastDoneState = doneData.state || null;
              lastDoneMemory = doneData.memory || null;
            } catch (_) {}
          } else if (eventName === "error" && dataStr) {
            try {
              const errPayload = JSON.parse(dataStr);
              const errMsg = errPayload.message || "Failed to generate reply.";
              showError(errMsg);
              fullReply += `\n[${errMsg}]`;
              asstElements.bodyText.textContent = fullReply;
            } catch (_) {}
          }
        }
      }

      // Stream completed
      if (cursor.parentNode) {
        cursor.parentNode.removeChild(cursor);
      }
      asstElements.bodyText.textContent = fullReply;

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
      if (currentSessionId) {
        refreshStateAndMemory(currentSessionId);
      }

      // Clear file selection
      filesInputEl.value = "";
      filesSelectedCountEl.textContent = "";
      loadSessions();

    } catch (err) {
      if (cursor.parentNode) {
        cursor.parentNode.removeChild(cursor);
      }
      const msg = err.message || "Failed to send message.";
      showError(msg);
      asstElements.bodyText.textContent = fullReply ? (fullReply + `\n[${msg}]`) : `[${msg}]`;
      asstElements.card.classList.add("interrupted");
    } finally {
      isStreaming = false;
      sendBtn.disabled = false;
      chatStatusEl.textContent = "Ready";
      chatStatusEl.className = "chat-status-badge";
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
      } catch (_) {}
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
