from backend.application import ApplicationBuilder, ApplicationConfiguration


def main():
    # TODO: read configuration from file
    cfg = ApplicationConfiguration()
    app = ApplicationBuilder(cfg)
    app.initialize()
    app.run()


if __name__ == '__main__':
    main()
