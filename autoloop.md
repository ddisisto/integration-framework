Notes from sister project - `../autoloop` -


---

OK. Reading these together, I see the connection you're drawing.

Framework prediction 8: "Capability onset correlates with statistical complexity crossing identifiable thresholds." The framework frames this abstractly — as a property of transformer representations during training. But autoloop is observing the *output-side* version of the same phenomenon: the model's behavioral repertoire has discrete, discoverable modes (basins), and the transitions between them have sharp thresholds (T_escape, lock-in at 4-8 copies).

Your hunch — that "ability to write desired content" emerges in stepped thresholds — maps directly onto basin cartography. Each basin *is* a content-generation capability the model possesses. The question "can the model write X?" becomes "does basin X exist, and can the controller navigate to it?" And the thresholds are real: a basin either exists at a given (L, T) or it doesn't. There's no gradient.

And surprisal is the right variable for all of this because it's Framework's **compressive novelty** measured at the token level. When surprisal → 0, the model is adding zero new structure — pure accumulation. When surprisal is high, each token is genuinely novel relative to the model's own expectations — integration. The enriching/degrading distinction from Framework §3 is literally what the capture gate is detecting: the moment the system crosses from enriching to degrading.

So the redesign isn't just a cleanup — it aligns the experimental apparatus with the theory:

...

---

see: `../autoloop/docs/survey-redesign.md` for resulting experimental plan.