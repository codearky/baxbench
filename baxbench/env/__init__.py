from .base import Env
from .go import FiberEnv, GinEnv, NetHttpEnv
from .javascript import ExpressEnv, FastifyEnv, KoaEnv, NestJsEnv
from .php import PhpLaravelLumenEnv
from .python import AioHttpEnv, DjangoEnv, FastAPIEnv, FlaskEnv
from .ruby import RubyOnRailsEnv
from .rust import RustActixEnv

all_envs: list[Env] = [
    AioHttpEnv,
    DjangoEnv,
    ExpressEnv,
    FastAPIEnv,
    FastifyEnv,
    FiberEnv,
    FlaskEnv,
    GinEnv,
    KoaEnv,
    NestJsEnv,
    NetHttpEnv,
    PhpLaravelLumenEnv,
    RubyOnRailsEnv,
    RustActixEnv,
]
