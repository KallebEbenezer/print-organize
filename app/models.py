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