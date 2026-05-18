import os
import psycopg2

from extract import extract
from transform import clean, aggregate_by_month
from load import (
    get_engine,
    create_tables,
    load_ventes,
    load_mart,
    log_etape
)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://etl_user:etl_secret@localhost:5432/warehouse"
)

CSV_PATH = "data/ventes.csv"


def main():

    print("=== Pipeline ETL ===")

    conn = psycopg2.connect(DATABASE_URL)
    engine = get_engine(DATABASE_URL)

    try:

        create_tables(conn)

        # EXTRACT
        print("\n[1/3] Extract")
        df_brut = extract(CSV_PATH)

        log_etape(conn, "extract", "success", len(df_brut))

        # TRANSFORM
        print("\n[2/3] Transform")
        df_clean = clean(df_brut)

        df_mart = aggregate_by_month(df_clean)

        log_etape(conn, "transform", "success", len(df_clean))

        # LOAD
        print("\n[3/3] Load")

        n1 = load_ventes(df_clean, engine)
        n2 = load_mart(df_mart, engine)

        log_etape(conn, "load", "success", n1 + n2)

        print("\nPipeline terminé")

    except Exception as e:

        log_etape(conn, "pipeline", "failure", message=str(e))

        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()