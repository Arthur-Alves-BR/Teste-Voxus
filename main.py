import sys

from kernel import exceptions
from controllers.active_controllers import controllers

if __name__ == '__main__':
    try:
        target = sys.argv[1]
    except IndexError as exc:
        raise exceptions.BAD_REQUEST_400() from exc

    for controller in controllers:
        if hasattr(controller, target):
            action = getattr(controller, target)
            action()
            sys.exit()

    raise exceptions.NOT_FOUND_404()
