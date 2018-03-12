import asyncio
import logging


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)


async def grandfather():
    log.info(f"grandfather: START")
    await father()
    log.info(f"grandfather: END")


async def father():
    log.info(f"father: START")
    await child()
    log.info(f"father: END")


async def child():
    log.info(f"child: START")
    await asyncio.sleep(3)
    log.info(f"child: END")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    log.info("main: START run_until_complete")
    loop.run_until_complete(grandfather())
    log.info("main: END   run_until_complete")
