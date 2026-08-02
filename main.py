from core.runtime import Runtime
from core.logger import info


def main():

    runtime = Runtime()

    try:

        runtime.initialize()

        runtime.run()

    except KeyboardInterrupt:

        log("\nShutdown requested.")

    finally:

        runtime.shutdown()


if __name__ == "__main__":
    main()