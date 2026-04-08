# Architecture Plan: "Windows-like but Better"

## 1. Dual-delivery model

My-OS now has two coordinated tracks:

1. **Web Desktop Track (current runnable build):** a GitHub Pages-hosted desktop shell with a Scramjet Browser app experience.
2. **Native OS Track (long-term):** Linux-based operating system with strong compatibility and security.

## 2. Web Desktop track (GitHub Pages)

### Goals
- Run instantly from static hosting.
- Provide OS-like UX (desktop, taskbar, app windows).
- Include a Scramjet-focused browser app entry point.

### Constraints
- Static pages cannot deliver full kernel or native driver control.
- Browser sandbox limitations apply.

## 3. Native OS track

### Kernel and base system
- Linux kernel for mature hardware compatibility.
- Custom userland shell/compositor and system services.
- Immutable signed A/B updates.

### Desktop stack
- Wayland compositor.
- GPU-accelerated UI toolkit.
- Sandboxed app model.

### Security
- Mandatory sandboxing for internet-facing apps.
- Signed metadata + reproducible builds.
- Clear runtime permissions.

## 4. Windows app and game compatibility

- Wine for general `.exe` apps.
- Proton + DXVK/VKD3D for game workloads.
- Compatibility manager service:
  - per-app prefixes,
  - runtime selection,
  - app-specific DLL/registry templates.

## 5. Scramjet browser direction

- Treat Scramjet as the default browser app slot in the web desktop.
- Long term: integrate privacy controls, anti-fingerprinting defaults, and hardened proxy chain workflows.

## 6. Delivery phases

### Phase 0 (current)
- GitHub Pages web desktop
- Scramjet app shell
- Wine/Proton launcher script

### Phase 1
- Installer ISO prototype
- Native shell + settings panel

### Phase 2
- Compatibility control center for Windows apps/games
- Telemetry-free diagnostics

### Phase 3
- LTS release channels and hardware certification
