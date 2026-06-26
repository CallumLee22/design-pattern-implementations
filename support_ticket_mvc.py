"""Support ticket implementation using the MVC pattern"""


# Model
class Ticket:
    def __init__(self, issue, level_required):
        self.issue = issue
        self.level_required = level_required


# View
class SupportView:
    @staticmethod
    def show_processing(ticket):
        print(f"Processing ticket: {ticket.issue}")

    @staticmethod
    def show_handled(level, ticket):
        print(f"Level {level} handled ticket: {ticket.issue}")

    @staticmethod
    def show_unhandled(ticket):
        print(f"Ticket: {ticket.issue} could not be handled")

    @staticmethod
    def show_escalation(from_level, to_level, ticket):
        print(
            f"Level {from_level} cannot handle '{ticket.issue}'. Escalating to Level {to_level}..."
        )


# Controller
class SupportController:
    def __init__(self, max_level=3):
        self.max_level = max_level

    def handle_ticket(self, ticket: Ticket):
        SupportView.show_processing(ticket)

        # Try to resolve at each level
        for level in range(1, self.max_level + 1):
            if ticket.level_required <= level:
                SupportView.show_handled(level, ticket)
                return
            else:
                if level < self.max_level:
                    SupportView.show_escalation(level, level + 1, ticket)

        # If no level can handle it
        SupportView.show_unhandled(ticket)


# App
controller = SupportController()
tickets = [
    Ticket("Password reset", 1),
    Ticket("Install VSCode", 2),
    Ticket("Server outage", 3),
    Ticket("Major complex issue", 4),
]
for ticket in tickets:
    controller.handle_ticket(ticket)
