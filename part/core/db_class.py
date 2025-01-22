from sqlalchemy.orm import Session

from menu.repositories import UserRepository, CustomerRepository

from admin.repositories import AdminRepository, SubscriptionRepository


class DBClass:
    def __init__(self, session: Session):
        # ADMIN APP
        self.admin = AdminRepository(session=session)
        self.subscription = SubscriptionRepository(session=session)

        # USER APP
        self.user = UserRepository(session=session)
        self.customer = CustomerRepository(session=session)