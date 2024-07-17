from utils.asyncio_helper import sleep


class UserManager:

    @classmethod
    async def signup(cls, params: dict) -> dict[str, str]:
        await sleep()
        print("Connecting to db.....")
        print(f"Inserting user details {params} to db")
        await sleep(delay=10)
        return {
            "msg": "Account created successfully"
        }


