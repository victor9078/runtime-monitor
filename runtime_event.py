class RuntimeEvent:

    def __init__(
        self,
        component,
        field,
        old,
        new
    ):
        self.component = component
        self.field = field
        self.old = old
        self.new = new
        
    def __str__(self):

        if self.field == "running":

            old = "Running" if self.old else "Stopped"
            new = "Running" if self.new else "Stopped"

            return f"{self.component}: {old} → {new}"

        return f"{self.component}: {self.field} {self.old} → {self.new}"