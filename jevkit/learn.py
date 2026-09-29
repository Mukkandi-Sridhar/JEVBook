"""Tiny, readable learning code used in Part I (logistic regression from scratch)."""

from __future__ import annotations

import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -35, 35)))


def log_loss(p, y):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


class Standardizer:
    def fit(self, X):
        self.mu, self.sd = X.mean(0), X.std(0) + 1e-9
        return self

    def __call__(self, X):
        return (X - self.mu) / self.sd


def fit_logistic(X, y, lr=0.5, steps=300, record=False):
    """Plain gradient descent on log loss. Returns (w, b, history)."""
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    w = np.zeros(X.shape[1])
    b = 0.0
    hist = []
    for _ in range(steps):
        p = sigmoid(X @ w + b)
        grad_w = X.T @ (p - y) / len(y)
        grad_b = float(np.mean(p - y))
        w -= lr * grad_w
        b -= lr * grad_b
        if record:
            hist.append(log_loss(p, y))
    return w, b, hist
