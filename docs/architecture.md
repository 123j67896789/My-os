# Architecture Plan: "Windows-like but Better"

## 1. Product goals

- Run a modern desktop UI with strong performance and security.
- Support legacy and modern apps, including Windows `.exe` and common game engines.
- Default privacy protections for users in surveillance-heavy environments.

## 2. Core platform strategy

### Kernel and base system
- Start from Linux kernel for hardware compatibility and driver maturity.
- Build a custom userland shell/compositor and system services.
- Use immutable system partitions + signed updates (A/B updates).

### Desktop stack
- Wayland-based compositor.
- GPU-accelerated UI toolkit.
- Sandboxed app model by default.

### Security
- Mandatory sandboxing for internet-facing apps.
- Signed package metadata and reproducible builds.
- Transparent permission prompts (camera, mic, files, network).

## 3. Windows app and game compatibility

### Compatibility layers
- Use Wine for general `.exe` compatibility.
- Use Proton + DXVK/VKD3D for game compatibility.
- Build a compatibility manager service:
  - per-app prefixes,
  - automatic runtime selection,
  - registry and DLL override templates.

### Game support details
- Prefer Vulkan path through DXVK/VKD3D.
- Integrate anti-cheat status checks and known-issues database.
- Add launcher profiles (FPS mode, latency mode, battery mode).

## 4. Privacy browser for surveillance states

### Design principles
- Default to proxy chain support (SOCKS5/HTTP upstream).
- Strip high-entropy headers and isolate cookie jars.
- Enforce HTTPS where possible.
- Disable WebRTC local IP leakage by default.

### Threat model assumptions
- ISP-level metadata collection.
- State DNS tampering/blocking.
- Network logging and selective censorship.

### Hardening roadmap
1. Multi-hop transport support.
2. Domain fronting alternatives where legal and viable.
3. Pluggable transport obfuscation.
4. Censorship-resilient update channels.

## 5. Delivery phases

### Phase 0 (current)
- Architecture, launcher script, privacy proxy starter.

### Phase 1
- Installer ISO prototype.
- Basic desktop shell and app store.

### Phase 2
- Compatibility control panel for `.exe` and games.
- Telemetry-free crash reporting.

### Phase 3
- Stable release with LTS channel.
