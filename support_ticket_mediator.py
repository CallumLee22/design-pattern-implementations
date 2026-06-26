"""Support ticket system using the mediator pattern"""

from abc import ABC, abstractmethod


class Ticket:
    def __init__(self, issue, level_required):
        self.issue = issue
        self.level_required = level_required


# Mediator
class SupportMediator:
    def __init__(self):
        self.handlers = []

    def register_handler(self, handler):
        self.handlers.append(handler)

    def process_ticket(self, ticket: Ticket):
        for handler in self.handlers:
            if handler.can_handle(ticket):
                handler.handle(ticket)
                return

        print(f"Ticket: {ticket.issue} could not be handled")


# Handlers
class SupportHandler(ABC):
    def __init__(self, mediator, level):
        self.mediator = mediator
        self.level = level
        mediator.register_handler(self)

    def can_handle(self, ticket: Ticket):
        return ticket.level_required <= self.level

    @abstractmethod
    def handle(self, ticket: Ticket):
        pass


# Concrete handlers
class Level1Support(SupportHandler):
    def __init__(self, mediator):
        super().__init__(mediator, level=1)

    def handle(self, ticket: Ticket):
        print(f"Level 1 handled ticket: {ticket.issue}")


class Level2Support(SupportHandler):
    def __init__(self, mediator):
        super().__init__(mediator, level=2)

    def handle(self, ticket: Ticket):
        print(f"Level 2 handled ticket: {ticket.issue}")


class Level3Support(SupportHandler):
    def __init__(self, mediator):
        super().__init__(mediator, level=3)

    def handle(self, ticket: Ticket):
        print(f"Level 3 handled ticket: {ticket.issue}")


mediator = SupportMediator()
# Register handlers with mediator
Level1Support(mediator)
Level2Support(mediator)
Level3Support(mediator)
tickets = [
    Ticket("Password reset", 1),
    Ticket("Install VSCode", 2),
    Ticket("Server outage", 3),
    Ticket("Major complex issue", 4),
]
for ticket in tickets:
    print(f"Processing ticket: {ticket.issue}")
    mediator.process_ticket(ticket)
