from UiLayer.UIMain import UIMain
from UiLayer.train import train

def build_app() -> UIMain:
    app: UIMain = UIMain()
    return app


def main() -> None:
    app: UIMain = build_app()
    train().runTrain()
    app.mainloop()


if __name__ == "__main__":
    main()
