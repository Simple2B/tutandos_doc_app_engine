from uuid import UUID


class ServiceDocument:
    def init_db(self, db):
        self.db = db

    def get_answers(self, audit_id: UUID):
        return self.db.get("Answers", {"audit_id": audit_id})

    def is_audit_exist(self, audit_id: UUID):
        audit = self.db.get("Audits", eq={"id": audit_id}, count=1)
        if audit:
            return audit[0]

        return False
