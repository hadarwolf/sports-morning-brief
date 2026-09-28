"use client";

import { useCallback, useState } from "react";

// All user state (preferences, streak, saved items) lives in this phone's localStorage.
// Reads and writes are wrapped: storage can throw in private mode or be cleared.

const PREFIX = "daily-brief:";

export function readStored<T>(key: string, fallback: T): T {
  try {
    const raw = localStorage.getItem(PREFIX + key);
    return raw === null ? fallback : (JSON.parse(raw) as T);
  } catch {
    return fallback;
  }
}

export function writeStored<T>(key: string, value: T): void {
  try {
    localStorage.setItem(PREFIX + key, JSON.stringify(value));
  } catch {
    // Not persisting is fine; the app still works for this session.
  }
}

/**
 * useState that persists to localStorage. Only use it in components whose prerendered
 * HTML doesn't depend on the value (the app prerenders just a loading screen), so the
 * stored value can be read on the first client render without a hydration mismatch.
 */
export function useStored<T>(key: string, fallback: T): [T, (value: T | ((prev: T) => T)) => void] {
  const [value, setValue] = useState<T>(() => (typeof window === "undefined" ? fallback : readStored(key, fallback)));

  const set = useCallback(
    (next: T | ((prev: T) => T)) => {
      setValue((prev) => {
        const resolved = typeof next === "function" ? (next as (p: T) => T)(prev) : next;
        writeStored(key, resolved);
        return resolved;
      });
    },
    [key],
  );

  return [value, set];
}
