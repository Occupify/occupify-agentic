# Game Developer

## Metadata
- Type: Role
- Domain: Game Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/game-developer
- Related Roles:
  - Backend Developer
  - Server Side Game Developer
  - Frontend Developer

---

## 1. Beginner

### 1.1 Client Side Development
- **Client Side Development**
  - Client side development in games refers to the code and systems that run on the player's machine, including rendering, input handling, audio, UI, and local game logic. It contrasts with server-side code in multiplayer games, which handles authoritative game state.

### 1.2 Game Mathematics
- **Linear Algebra**
  - Linear algebra is the branch of mathematics dealing with vectors, matrices, and linear transformations. In game development it is used for nearly every spatial calculation, including position, direction, rotation, scaling, and projection.
- **Matrix**
  - A matrix is a rectangular array of numbers used to represent linear transformations in 2D and 3D space. In games, matrices are used to transform vertices from object space to world space, view space, and clip space through multiplication.
- **Linear Transformation**
  - A linear transformation is a mapping between vector spaces that preserves vector addition and scalar multiplication. In games, linear transformations include rotation, scaling, and shearing, represented as matrix multiplications.
- **Affine Space**
  - An affine space extends a vector space by adding points that represent positions rather than directions. The key distinction is that two points can be subtracted to produce a vector, but two points cannot be added to each other.
- **Affine Transformation**
  - An affine transformation combines linear transformations like rotation and scaling with translation, mapping points from one coordinate space to another while preserving parallelism and ratios of distances along lines. In games, affine transformations are represented using 4x4 matrices in homogeneous coordinates.
- **Center of Mass**
  - The center of mass is the average position of all the mass in an object, weighted by each part's mass. In rigid body simulation, forces applied at the center of mass produce pure linear acceleration with no rotation, while forces applied off-center also generate torque.
- **Moment of Inertia**
  - The moment of inertia is the rotational analog of mass, describing how resistant an object is to changes in its rotational motion. It depends on both the object's mass and how that mass is distributed relative to the axis of rotation.

### 1.3 Projection
- **Vector**
  - A vector is a mathematical object with both magnitude and direction, represented as an ordered list of numbers. In 3D game development, vectors are used to represent positions, velocities, normals, and forces.
- **Geometry**
  - Geometry in game development covers the mathematical description of shapes, surfaces, and spatial relationships. Topics include point-line-plane tests, polygon representations, mesh structures, and computational geometry algorithms.
- **Perspective**
  - Perspective projection simulates how objects appear smaller as they move farther from the camera, matching the behavior of real optical systems. It maps 3D points into 2D screen space by dividing x and y by z, producing a view frustum shape.
- **Orthogonal**
  - Orthographic projection maps 3D coordinates to 2D screen space without any depth-based scaling, so objects appear the same size regardless of their distance from the camera. It is used in 2D games, isometric views, engineering visualizations, and shadow map generation for directional lights.

### 1.4 Orientation
- **Quaternion**
  - A quaternion is a four-component number system used to represent 3D rotations. Quaternions avoid gimbal lock, interpolate smoothly using SLERP, and are more numerically stable than Euler angles for accumulated rotations.
- **Euler Angle**
  - Euler angles represent a 3D rotation as three sequential rotations around the coordinate axes, typically labeled pitch, yaw, and roll. They are intuitive for humans to read and author but suffer from gimbal lock, where two rotation axes align and a degree of freedom is lost.

---

## 2. Intermediate

### 2.1 Curve
- **Spline**
  - A spline is a piecewise polynomial curve defined by multiple segments that connect smoothly at their joining points. In games, splines are used to define camera paths, character motion trajectories, and procedural level geometry.
- **Hermite**
  - A Hermite curve is a cubic polynomial segment defined by its two endpoints and the tangent vectors at each endpoint. The tangent vectors control the direction and speed at which the curve leaves and arrives at each point.
- **Bezier**
  - A Bezier curve is defined by a set of control points where the first and last points lie on the curve and the intermediate points act as attractors that shape the path. Cubic Bezier curves are the most common, defined by four control points, and are used extensively in vector graphics, animation tools, and path generation.
- **Catmull-Rom**
  - A Catmull-Rom spline is a type of cubic spline that passes through all of its control points, making it convenient for path interpolation. Unlike Bezier curves, no separate tangent handles are needed because the tangents are computed automatically from the surrounding control points.

### 2.2 Dynamics
- **Acceleration**
  - Acceleration is the rate of change of velocity over time, produced by a net force acting on an object according to Newton's second law. In game physics, acceleration is computed from the sum of all forces applied to a body divided by its mass, then integrated to update velocity.
- **Joints**
  - Joints, also called constraints, connect two rigid bodies and restrict their relative motion to a defined set of degrees of freedom. Common joint types include hinge joints that allow rotation around one axis, ball-and-socket joints that allow rotation in all directions, and slider joints that allow linear movement along an axis.
- **Force**
  - A force is a vector quantity that causes a change in an object's momentum when applied to it. In rigid body simulation, forces are accumulated each frame and integrated to produce acceleration and velocity changes.
- **Restitution**
  - Restitution, or the coefficient of restitution, describes how much kinetic energy is preserved after a collision between two objects. A value of 1 represents a perfectly elastic collision with no energy loss, while 0 represents a perfectly inelastic collision where objects do not bounce.
- **Angular Velocity**
  - Angular velocity is the rate at which an object rotates, represented as a vector whose direction is the axis of rotation and whose magnitude is the rotation speed in radians per second. In rigid body simulation, angular velocity is updated by integrating applied torques and is used to advance the object's orientation each frame.
- **Buoyancy**
  - Buoyancy is the upward force exerted on an object submerged in a fluid, equal to the weight of the fluid displaced. In game physics, buoyancy is approximated by applying an upward force proportional to the submerged volume of an object below a water surface plane.
- **Linear Velocity**
  - Linear velocity is the rate of change of an object's position over time, represented as a vector indicating speed and direction of movement. In rigid body simulation, linear velocity is updated each frame by integrating applied forces and is used to advance the object's position.
- **Friction**
  - Friction is the force that opposes relative motion between surfaces in contact. In game physics, two types are modeled: static friction, which prevents an object from starting to slide, and kinetic friction, which opposes sliding motion.

### 2.3 Game Physics
- **Game Physics**
  - Game physics simulates physical behavior in a game world, including rigid body dynamics, collision detection, constraints, and fluid or soft body effects. Physics engines abstract the mathematics of Newtonian mechanics into systems that update object positions and velocities each frame.

### 2.4 Game Engine
- **SAT**
  - The Separating Axis Theorem (SAT) is a method for detecting collisions between convex shapes. It works by testing a set of axes and checking whether the projections of two shapes onto each axis overlap.
- **Godot**
  - Godot is an open-source, multi-platform game engine that is known for being feature-rich and user-friendly. It is developed by hundreds of contributors from around the world and supports the creation of both 2D and 3D games.
- **Unreal Engine**
  - The Unreal Engine is a powerful game development engine created by Epic Games. Used by game developers worldwide, it supports the creation of high-quality games across multiple platforms such as iOS, Android, Windows, Mac, Xbox, and PlayStation.
- **Native**
  - You don't necessarily have to use tools like Unreal, Unity3d, or Godot to make games. You can also use native languages like C++ or Rust to make games.
- **Unity 3D**
  - Unity 3D is a versatile, cross-platform game engine that supports the development of both 2D and 3D games. This game engine allows users to create a wide variety of games including AR, VR, Mobile, Consoles, and Computers in C#.

### 2.5 Collision Detection
- **Narrow Phase**
  - Narrow phase collision detection performs precise geometric intersection tests between pairs of objects that the broad phase has flagged as potential collisions. It computes contact points, contact normals, and penetration depths needed for the physics solver.
- **Broad Phase**
  - Broad Phase Collision Detection is the first step in the collision detection process. Its primary function is to identify which pairs of objects might potentially collide.
- **Convexity**
  - Convexity describes the property of a shape where any line segment connecting two points inside the shape remains entirely inside it. Convex shapes are simpler to process in physics simulations because algorithms like GJK can solve intersection and distance queries efficiently for them.
- **Convex**
  - The term "convex" in game development relates primarily to shapes and collision detection within the gaming environment. A shape is convex if all line segments between any two points in the shape lie entirely within the shape.
- **Concave**
  - A concave shape has at least one surface that curves inward, meaning a line segment between two interior points may pass outside the boundary. Concave meshes cannot be used directly in many physics algorithms without decomposition.
- **Intersection**
  - Intersection tests determine whether two geometric shapes overlap in space. These tests are used throughout physics and rendering to answer questions like whether a ray hit a surface or whether two colliders are touching.
- **Bounding Volume**
  - Bounding Volume is a simple shape that fully encompasses a more complex game model. It is less expensive to check for the intersection of bounding volumes when compared to checking for intersection of the actual models.
- **AABB**
  - An AABB (Axis-Aligned Bounding Box) is a rectangular bounding volume whose edges are always aligned with the world coordinate axes. It is one of the simplest and fastest bounding volume types to compute and test for overlap.
- **OBB**
  - An OBB (Oriented Bounding Box) is a rectangular bounding volume that can rotate freely to match the orientation of the object it encloses. Compared to an AABB, an OBB typically provides a tighter fit, reducing false positives in collision tests.
- **Spatial Partitioning**
  - Spatial partitioning divides a scene into regions to accelerate queries like collision detection, ray casting, and visibility culling. By organizing objects into a structure that reflects their position in space, the engine can quickly discard large portions of the scene that are irrelevant to a given query.
- **CCD**
  - Continuous Collision Detection (CCD) prevents fast-moving objects from tunneling through thin geometry by testing for collisions along the entire swept path of an object between frames, rather than just at the start and end positions. Without CCD, a bullet or fast projectile can pass entirely through a wall in a single time step.

### 2.6 Programming Languages
- **Convex Hull**
  - A convex hull is the smallest convex shape that fully contains a set of points. In game development, convex hulls are generated from mesh vertices to produce physics colliders that approximate the original shape while remaining usable by convex-only physics algorithms.
- **Convex Decomposition**
  - Convex decomposition breaks a concave mesh into a set of convex pieces that together approximate the original shape. This allows concave objects to be simulated in physics engines that require convex geometry by treating the decomposed parts as a compound collider.
- **GJK**
  - The GJK algorithm (Gilbert–Johnson–Keerthi) is a computational geometry algorithm that is widely used to detect collisions between convex objects in video games and simulations. The primary role of this algorithm is to assess the intersection between two convex shapes.
- **EPA**
  - The EPA (Expanding Polytope Algorithm) is an iterative algorithm used for calculating the penetration depth between two shapes in collision detection. It is commonly used in physics engines and robotics.
- **C/C++**
  - C and C++ are the dominant languages for game engine development and performance-critical game code. C++ offers object-oriented features, templates, and direct memory management, making it suitable for building engines, physics systems, and rendering pipelines.
- **C#**
  - C# is a statically typed, object-oriented language developed by Microsoft and used as the primary scripting language in Unity. It runs on the .NET runtime and features garbage collection, LINQ, and strong tooling support.
- **GDScript**
  - GDScript is the primary scripting language for the Godot game engine, designed to be easy to learn and tightly integrated with the engine's node system. Its syntax resembles Python, making it accessible to beginners while remaining capable enough for production games.
- **Rust**
  - Rust is a systems programming language focused on memory safety and performance without a garbage collector. In game development, Rust is used for engine components, tools, and increasingly for full game projects through frameworks like Bevy.
- **Python**
  - Python is a high-level, dynamically typed language used in game development primarily for tooling, automation, and scripting. Its readable syntax and large standard library make it practical for build pipelines, content generation, and prototype logic.

---

## 3. Advanced

### 3.1 Computer Graphics
- **Sort & Sweep**
  - Sort and sweep, also called sweep and prune, is a broad-phase collision detection technique. Objects' bounding volumes are projected onto one or more axes, and the projections are sorted.
- **BVH**
  - A BVH (Bounding Volume Hierarchy) is a tree structure where leaf nodes contain individual objects and each internal node contains a bounding volume that encloses all its children. BVHs are widely used for ray tracing and broad-phase collision detection.
- **DBVT**
  - A DBVT (Dynamic Bounding Volume Tree) is a variant of BVH designed for scenes where objects move frequently. Rather than rebuilding the entire tree on each frame, a DBVT supports incremental updates by reinserting or refitting only the affected nodes.
- **Ray Tracing**
  - Ray tracing is a rendering technique that simulates light by tracing paths from the camera through each pixel into the scene, calculating intersections with geometry and recursively following reflected, refracted, and shadow rays. It produces physically accurate shadows, reflections, and global illumination but is computationally expensive.
- **Rasterization**
  - Rasterization is the standard rendering technique used in real-time graphics, where 3D geometry is projected onto a 2D screen and filled with pixel colors based on shading calculations. It is much faster than ray tracing but requires additional techniques like shadow mapping, screen-space reflections, and ambient occlusion to approximate lighting effects that ray tracing handles natively.
- **Graphics Pipeline**
  - The graphics pipeline is the sequence of stages that transforms 3D geometry into a final 2D image on screen. It includes stages like vertex processing, rasterization, fragment shading, and output merging.
- **Sampling**
  - Sampling in graphics refers to how discrete values are taken from continuous signals such as textures or light distributions. Aliasing artifacts appear when a scene contains detail at frequencies higher than the sampling rate, which is why techniques like multisampling, supersampling, and temporal anti-aliasing are used.
- **Shader**
  - Shaders are a type of software used in 3D computer graphics. They are utilized to render quality visual effects by making calculations and transformations on image data.
- **Rendering Equation**
  - The rendering equation, introduced by Kajiya in 1986, describes the total light leaving a surface point in a given direction as the sum of emitted light and incoming light reflected from all directions. It provides the theoretical basis for physically based rendering.
- **Computer Animation**
  - Computer animation covers techniques for producing motion in 3D scenes, including skeletal animation, blend shapes, procedural animation, and physics-based simulation. In games, animation systems must run in real time and blend smoothly between different motion clips based on gameplay state.
- **Color**
  - Color in computer graphics is represented using color models such as RGB, HSV, and CIELAB, each suited to different tasks. Understanding color spaces, gamma correction, and the difference between linear and perceptual workflows is important for producing consistent results across displays and rendering pipelines.
- **Visual Perception**
  - Visual perception in graphics refers to how the human visual system interprets rendered images, including sensitivity to contrast, color, motion, and depth. Rendering techniques are often designed to exploit or match perceptual characteristics rather than achieve physical accuracy.
- **Tone Reproduction**
  - Tone reproduction, also called tone mapping, is the process of converting high dynamic range (HDR) scene luminance values into the limited range that a display can show. Since real-world lighting varies across many orders of magnitude, tone mapping operators compress this range while preserving perceived contrast and detail.
- **Lighting and Shadow**
  - Lighting and shadow systems determine how light sources illuminate a scene and how objects block that light to cast shadows. Real-time engines use a combination of dynamic lights, shadow maps, and baked light data to balance visual quality and performance.
- **Shadow Map**
  - A shadow map is a depth texture rendered from the light's point of view, used to determine which parts of the scene are in shadow when rendering from the camera. Each fragment is compared to the stored depth value; if it is farther from the light than what the shadow map records, it is shadowed.
- **2D**
  - 2D Game Development involves creating games in a two-dimensional plane, utilizing flat graphics and typically making use of x and y coordinates. From classic arcade games of the ’80s and ’90s to the rich array of indie games today, 2D game development is a vibrant and diverse sector of the gaming industry.
- **Cube**
  - In computer graphics, "cube" in the context of shadows often refers to using a cube-shaped object to visualize the concept of a "shadow volume." Imagine a light source shining on a cube. The silhouette of the cube from the light's perspective, extended infinitely outwards, forms a volume.
- **Cascaded**
  - Cascaded usually refers to cascaded shadow maps, a technique for rendering realistic shadows over a large area.
- **Light Source**
  - A light source in 3D rendering is an entity that emits light and contributes to the illumination of the scene. Different light types produce different shading and shadow characteristics and must be configured according to the lighting design of the scene.
- **Directional**
  - Directional light simulates a distant light source like the sun. It has only a direction, not a specific position, meaning its light rays are parallel and cast consistent shadows regardless of object location within the scene.
- **Point**
  - Point lights are one of the most common types of lights used in computer graphics and games. They resemble real-world light bulbs, emitting light uniformly in all directions.
- **Spot**
  - Spotlights are a common type of light in computer graphics and games that mimic the behavior of real-world spotlights. They offer a range of parameters to adjust their behavior, such as radius, cone angle, falloff, and intensity Spotlights are readily available out of the box in both Unreal and Unity game engines, making them an accessible and powerful tool for adding realistic and dynamic lighting to your scenes.
- **Infinite**
  - Infinite refers to concept that deals with rendering scenes or objects that extend beyond the visible boundaries of the screen. This is crucial for creating immersive environments, as it allows developers to simulate vast landscapes or endless spaces without the need to render every detail at once.
- **Stencil Shadow**
  - Stencil shadows, also called shadow volumes, are a technique where the shadow boundary of an object is extruded into a volume and used to mark shadowed pixels in the stencil buffer. For each fragment, the algorithm counts how many shadow volumes surround it to determine whether it is in shadow.
- **HLSL**
  - HLSL (High-Level Shader Language) is the shader programming language used with DirectX. It compiles to GPU bytecode and supports all shader stages including vertex, pixel, compute, and ray tracing shaders.
- **GLSL**
  - GLSL (OpenGL Shading Language) is the shader language for OpenGL and Vulkan (via SPIR-V compilation). It follows a C-like syntax and supports vertex, fragment, geometry, tessellation, and compute shader stages.
- **SPIR-V**
  - SPIR-V is a binary intermediate language for graphics and computation kernels, which is defined by the Khronos Group. This programming language has been largely adopted and used by Vulkan, a low-overhead, cross-platform 3D graphics and computing API.

### 3.2 Graphics API
- **Reflection**
  - Reflection describes how light bounces off a surface back toward the viewer. In real-time rendering, reflections are approximated using techniques like cube maps, screen-space reflections, and planar reflection textures.
- **Diffuse**
  - In the world of 3D rendering and game development, "diffuse" refers to diffuse lighting or diffuse reflection. It's a key concept in making objects look three-dimensional and realistically lit.
- **Specular**
  - Specular reflections are mirror-like reflections. In these cases, the rays of light are reflected, more than they are absorbed.
- **Mapping**
  - Mapping in graphics refers to techniques that apply 2D images or data to 3D surfaces to add detail without increasing geometry count. Texture mapping, normal mapping, parallax mapping, and horizon mapping are all variations that serve different purposes, from adding color and surface texture to simulating depth and complex lighting responses.
- **Texture**
  - Textures are 2D images applied to 3D surfaces to provide color, detail, or surface data like roughness and normals. They are sampled by shaders during rendering using UV coordinates mapped onto geometry.
- **Bump**
  - Bump mapping is a technique that perturbs surface normals at the pixel level to create the illusion of small-scale surface detail without adding geometry. The original method stored height values in a grayscale texture and derived normals from it.
- **Parallax**
  - Parallax mapping is an enhancement over bump and normal mapping that offsets UV coordinates based on a height map and the viewing angle, giving surfaces a greater sense of depth. At steep angles, basic parallax mapping breaks down, so variants like parallax occlusion mapping add iterative ray stepping to improve accuracy for surfaces with significant height variation.
- **Horizon**
  - In graphics, the horizon refers to a horizontal line that represents the visual boundary where the sky meets the earth or a flat surface, such as the ocean. It's a fundamental concept in perspective and art, serving as a reference point for creating a sense of depth and distance in an image.
- **Visibility and Occlusion**
  - Visibility and occlusion systems determine which parts of a scene are visible from the camera and which are hidden behind other geometry. These systems are used to skip rendering work for geometry that cannot be seen, improving performance.
- **Occluder**
  - An occluder is a piece of geometry that blocks the view of objects behind it. In occlusion culling systems, occluders are used to test whether other objects are hidden and can therefore be skipped during rendering.
- **Culling**
  - Culling is a performance optimization strategy employed in game development to improve efficiency and speed. Culling helps in reducing the rendering workload by eliminating the elements that are not visible to the player or are outside the viewport of the game.
- **Clipping**
  - Culling is the process of eliminating geometry that does not need to be rendered, either because it is outside the view frustum, occluded by other objects, or facing away from the camera. Effective culling reduces the number of draw calls and the amount of geometry the GPU must process.
- **Fog**
  - Fog in game development refers to a visual effect used to simulate atmospheric conditions and enhance the depth perception in a game environment. It creates a gradient of visibility, often fading objects into the background, which can improve performance by reducing the number of objects rendered at a distance.
- **DirectX**
  - DirectX is a collection of Application Programming Interfaces (APIs) developed by Microsoft to handle tasks related to multimedia, especially game programming and video, on Microsoft platforms. It was first introduced in 1995 and has become a crucial component for PC gaming.
- **OpenGL**
  - OpenGL is a cross-platform graphics API that provides a high-level interface for 2D and 3D rendering. It has been widely used in games and applications since the 1990s but has largely been superseded by Vulkan for high-performance use cases.
- **OpenGL ES**
  - OpenGL ES (Open Graphics Library for Embedded Systems) is a subset of the OpenGL specification designed specifically for mobile and embedded devices, such as smartphones, tablets, and consoles. It provides a cross-platform API that allows developers to communicate directly with the device's Graphics Processing Unit (GPU) to render 2D and 3D computer graphics.
- **Vulkan**
  - Vulkan is a low-level, cross-platform graphics API developed by the Khronos Group. It offers explicit control over GPU memory, synchronization, and command submission, reducing driver overhead compared to OpenGL.

### 3.3 Game AI
- **Frustum**
  - Frustum culling is a standard practice in computer graphics, used in virtually all games to optimize performance by not rendering objects outside of your field of view. Think of your field of view as a frustum, a truncated pyramid shape.
- **Light**
  - Light refers to a visual representation of illumination in a 3D environment. It is used to simulate the way light behaves in the real world, adding depth, volume, and realism to objects and scenes.
- **Shadow**
  - Shadows play a crucial role in enhancing the realism and depth of scenes in video games. They help to create a more immersive experience by simulating how light interacts with objects in a 3D environment.
- **Polygon**
  - In computer graphics and game development, a polygon is a 2D or 3D shape composed of a set of vertices connected by edges. Polygons are used to represent objects, characters, and environments in games and simulations.
- **Polyhedron**
  - In computer graphics and game development, a polyhedron is a 3D shape composed of a set of polygons that enclose a volume. Polyhedra are used to represent objects, characters, and environments in games and simulations.
- **WebGL**
  - WebGL is a JavaScript API for rendering 2D and 3D graphics in a browser using the GPU, based on OpenGL ES 2.0 and 3.0. It runs without plugins and is supported in all major browsers.
- **Metal**
  - Metal is Apple's low-level graphics and compute API for iOS, macOS, iPadOS, and tvOS. It provides direct access to the GPU with minimal driver overhead and integrates tightly with Apple's hardware and development tools.
- **Decision Making**
  - Decision making in game AI governs how an NPC chooses what action to take based on its current state and environment. The goal is to produce behavior that appears intelligent and responsive to the player without being predictable or computationally expensive.
- **Decision Tree**
  - A decision tree is a hierarchical structure where each node tests a condition and branches to different subtrees based on the result. In game AI, decision trees are used to encode rules that determine NPC behavior, such as whether to attack, flee, or patrol.
- **Movement**
  - Movement in game AI covers how characters navigate and move through the game world. This includes steering behaviors for local movement, pathfinding for navigating around obstacles, and crowd simulation for managing groups of agents.
- **Decision Learning**
  - Decision learning refers to machine learning approaches that train models to make sequential choices, often in the form of learned decision trees or policy networks. In game contexts, it can be used to build NPCs that adapt their decision-making based on observed outcomes.
- **Naive Bayes Classifier**
  - A Naive Bayes classifier is a probabilistic model that predicts class membership based on Bayes' theorem with the assumption that features are conditionally independent. In games, it can be used for tasks like recognizing player behavior patterns or classifying game states.

### 3.4 Game AI
- **State Machine**
  - A finite state machine (FSM) is a model where an entity can exist in one of a finite set of states and transitions between states based on defined conditions. In game AI, FSMs control character behavior by mapping states like idle, patrol, and attack to specific actions and defining the triggers that switch between them.
- **Behavior Tree**
  - A behavior tree is a hierarchical control structure used to define complex NPC behaviors through composable nodes. Internal nodes like sequences, selectors, and decorators control the flow of execution, while leaf nodes represent individual actions or conditions.
- **Fuzzy Logic**
  - Fuzzy logic allows AI systems to work with degrees of truth rather than binary true/false values. In games, it is used to make NPC decision-making more gradual and natural, for example allowing a character to be "somewhat aggressive" rather than simply aggressive or not.
- **Markov System**
  - A Markov system in game AI models behavior as a set of states with probabilistic transitions between them. At each step, the system transitions to the next state based on probability weights, producing varied and non-deterministic NPC behavior.
- **Board Game**
  - Board game AI refers to techniques for building agents that play turn-based strategy games like chess, checkers, Go, and similar abstractions. These games have well-defined rules and discrete state spaces, making them natural benchmarks for AI algorithms.
- **Minimax**
  - Minimax is an artificial intelligence (AI) decision-making algorithm mainly used in decision making and game theory, particularly for two player zero-sum games. It formulates a strategy by simulating all possible game scenarios and assuming that the opponent is playing an optimal game.
- **AB Pruning**
  - Alpha-beta pruning is an optimization of the minimax algorithm that eliminates branches of the game tree that cannot influence the final decision. It maintains two values, alpha and beta, representing the minimum score the maximizing player is assured and the maximum score the minimizing player is assured.
- **MCTS**
  - Monte Carlo Tree Search (MCTS) is a search algorithm that builds a game tree by randomly simulating game play-outs and using the results to guide further exploration. It balances exploration of unknown branches with exploitation of known good moves using the UCB1 formula.
- **Decision Tree Learning**
  - Decision tree learning is a supervised machine learning method that builds a tree model from labeled training data by recursively splitting the data on the most informative features. In game AI, it can be used to learn behavior rules from recorded gameplay or designer-specified examples.
- **Deep Learning**
  - Deep learning uses neural networks with many layers to learn hierarchical representations of data. In game development, deep learning is applied to tasks like AI game agents, procedural content generation, animation synthesis, and image upscaling.
- **Reinforcements Learning**
  - Reinforcement learning (RL) trains an agent to maximize a cumulative reward signal by taking actions in an environment and observing the results. In games, RL has been used to train superhuman game-playing agents and is increasingly used for NPC behavior, playtesting, and animation control.
- **Learning**
  - Machine Learning is a field of study that gives computers the ability to learn without being explicitly programmed. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention.

### 3.5 Advanced Rendering
- **Goal Oriented Behavior**
  - Goal oriented behavior in game development refers to the artificial intelligence algorithms employed that give non-player characters (NPCs) the ability to make decisions based on certain objectives or tasks. These NPCs analyze the circumstances in the game environment, formulate a plan to achieve specific goals, and then execute it.
- **Artificial Neural Network**
  - An artificial neural network (ANN) is a computational model loosely inspired by biological neurons, consisting of layers of interconnected units that process input signals and produce outputs. Neural networks are trained by adjusting weights through backpropagation to minimize prediction error.
- **Real-time Ray Tracing**
  - Real-time ray tracing uses dedicated hardware acceleration, such as NVIDIA RTX or AMD RDNA ray tracing cores, to trace rays into the scene at interactive frame rates. It enables effects like accurate reflections, shadows, and ambient occlusion that are difficult to fake convincingly with rasterization.
- **DirectX Ray Tracing**
  - DirectX Raytracing (DXR) is Microsoft's extension to Direct3D 12 that exposes hardware ray tracing capabilities through a set of new pipeline stages and shader types including ray generation, intersection, any-hit, closest-hit, and miss shaders. DXR integrates ray tracing into the existing D3D12 rendering pipeline and is available on Windows 10 and later.
- **Vulkan Ray Tracing**
  - Vulkan Ray Tracing is the Khronos Group's extension to Vulkan that exposes hardware-accelerated ray tracing across platforms. It uses the same shader stage model as DXR and supports acceleration structure management for efficient scene traversal.
- **OptiX**
  - OptiX is NVIDIA's GPU-accelerated ray tracing API and SDK, designed for high-performance offline and real-time ray tracing on CUDA-capable hardware. It provides a programmable pipeline for ray tracing with support for custom intersection, shading, and miss programs.
- **Physically-Based Rendering**
  - Physically-based rendering (PBR) is a shading approach that models the interaction of light with surfaces based on physical principles such as energy conservation and the Fresnel effect. It uses standardized material parameters like base color, roughness, and metalness, which produce consistent results under different lighting conditions.
- **Translucency & Transparency**
  - Translucency and transparency describe different ways light passes through a material. Transparent materials allow light to pass through without scattering, like glass, while translucent materials scatter light as it passes through, like skin or wax.
- **Conservation of Energy**
  - Conservation of energy in rendering means that a surface cannot reflect more light than it receives. PBR shading models enforce this principle by ensuring that the sum of diffuse and specular contributions does not exceed the incoming irradiance.
- **Metallicity**
  - Metallicity, also called metalness, is a PBR material parameter that describes whether a surface behaves like a metal or a dielectric. Metals have no diffuse component and highly colored specular reflections, while dielectrics have diffuse color and white specular highlights.
- **Microsurface Scattering**
  - Microsurface scattering describes how light interacts with the microscopic irregularities of a surface, which are too small to model with geometry but affect the overall reflectance. PBR materials use microfacet models like GGX or Beckmann to represent the statistical distribution of these tiny surface normals.

---

## 4. Optional / Specialized Topics

- Affine Transformation
- Center of Mass
- Moment of Inertia
- Angular Velocity
- Buoyancy
- Linear Velocity
- Friction
- Unity 3D
- Concave
- Intersection
- Bounding Volume
- AABB
- OBB
- Spatial Partitioning
- CCD
- C/C++
- C#
- GDScript
- Rust
- Python
- Rasterization
- Graphics Pipeline
- Sampling
- Shader
- Rendering Equation

---

## 5. References

- [Game Developer Roadmap](https://roadmap.sh/game-developer)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Server Side Game Developer
- Frontend Developer

### Related Skills
- React Native
- Python
- JavaScript