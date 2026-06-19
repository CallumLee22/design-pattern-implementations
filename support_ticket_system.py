"""
This support ticket system implementation uses the chain of responsibility pattern
"""

from abc import ABC, abstractmethod


class Ticket:
    """Class to represent a support ticket"""

    def __init__(self, issue, level_required):
        self.issue = issue
        self.level_required = level_required


class SupportHandler(ABC):
    """An abstract handler class for handlers to implement"""

    def __init__(self, level):
        self.level = level
        self.next_handler = None

    @abstractmethod
    def process(self, ticket: Ticket):
        """Process the support ticket"""

    def set_next(self, handler):
        """
        Set the next handler so it knows where to send the ticket to if needed
        """
        self.next_handler = handler
        return handler

    def handle(self, ticket: Ticket):
        """Handle the support ticket"""
        if ticket.level_required <= self.level:
            self.process(ticket)
        elif self.next_handler:
            print(
                f"{self.__class__.__name__} cannot handle {ticket.issue}. Escalating..."
            )
            self.next_handler.handle(ticket)
        else:
            print(f"Ticket: {ticket.issue} could not be handled")


class Level1Support(SupportHandler):
    """Class to handle level 1 tickets"""

    def __init__(self):
        super().__init__(level=1)

    def process(self, ticket: Ticket):
        print(f"Level 1 handled ticket: {ticket.issue}")


class Level2Support(SupportHandler):
    """Class to handle level 2 tickets"""

    def __init__(self):
        super().__init__(level=2)

    def process(self, ticket: Ticket):
        print(f"Level 2 handled ticket: {ticket.issue}")


class Level3Support(SupportHandler):
    """Class to handle level 3 tickets"""

    def __init__(self):
        super().__init__(level=3)

    def process(self, ticket: Ticket):
        print(f"Level 3 handled ticket: {ticket.issue}")


if __name__ == "__main__":
    # Setup chain
    level1 = Level1Support()
    level2 = Level2Support()
    level3 = Level3Support()

    level1.set_next(level2).set_next(level3)

    tickets = [
        Ticket("Password reset", 1),
        Ticket("Install VSCode", 2),
        Ticket("Server outage", 3),
        Ticket("Major complex issue", 4),
    ]

    for ticket in tickets:
        print(f"Processing ticket: {ticket.issue}")
        level1.handle(ticket)
