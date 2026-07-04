# ADR-0002

## Title

Business Logic Resides in the Service Layer

## Status

Accepted

## Decision

Business rules such as assigning default status, generating UUIDs, and setting creation timestamps are implemented in the Service Layer.

## Rationale

This keeps API routing thin, repositories focused on persistence, and business rules centralized.

## Consequences

Business logic is easier to test and maintain.
