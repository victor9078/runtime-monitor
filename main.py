from core.runtime import Runtime


def main():

    runtime = Runtime()

    try:

        runtime.initialize()

        runtime.run()

    except KeyboardInterrupt:

        print("\nShutdown requested.")

    finally:

        runtime.shutdown()


if __name__ == "__main__":
    main()