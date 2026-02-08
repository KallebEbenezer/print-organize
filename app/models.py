from database import get_connection

class Area:
    @staticmethod
    def create(name: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO areas (name) VALUES (?)",
            (name,)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def list_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM areas ORDER BY name")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete(area_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM areas WHERE id = ?",
            (area_id,)
        )
        conn.commit()
        conn.close()

class Discipline:

    @staticmethod
    def create(area_id: int, name: str, save_path: str = None):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO disciplines (area_id, name, save_path) VALUES (?, ?, ?)",
            (area_id, name, save_path)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def list_by_area(area_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        rows = cursor.execute(
            """
            SELECT id, name, save_path
            FROM disciplines
            WHERE area_id = ?
            ORDER BY id DESC
            """,
            (area_id,)
        ).fetchall()

        conn.close()
        return rows

    @staticmethod
    def delete(discipline_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM disciplines WHERE id = ?",
            (discipline_id,)
        )

        conn.commit()
        conn.close()
