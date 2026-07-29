# ADD-002 — Service Manager

## Status

Accepted

## Context

The system now contains multiple long-running services.

Without a manager, the kernel would become responsible for
starting and stopping every component individually.

## Decision

Introduce a ServiceManager.

Responsibilities

- register services
- start services
- stop services
- expose service status

## Consequences

Advantages

- simpler kernel
- standardized lifecycle
- easier monitoring
- plugin support later

Disadvantages

- one extra abstraction layer
