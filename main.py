from hashlib import new
from hashlib import algorithms_available
from pathlib import Path


class Integrity:

    @staticmethod
    def hash_file(filename: str, algorithm: str = "sha256") -> str:
        try:
            if algorithm.lower() not in algorithms_available:
                raise ValueError(
                    "Unsupported hashing algorithm: {}".format(algorithm.lower())
                )

            hash_obj = new(name=algorithm.lower())

            CHUNK_SIZE: int = 65536  # 64 KB

            with open(file=filename, mode="rb") as file:
                while True:
                    chunk: bytes = file.read(CHUNK_SIZE)

                    if not chunk:
                        break

                    hash_obj.update(chunk)

            return hash_obj.hexdigest()

        except Exception as error:
            raise RuntimeError(error)

    @staticmethod
    def verify_integrity(file1: str, file2: str) -> str:
        try:
            hash1: str = Integrity.hash_file(filename=file1)
            hash2: str = Integrity.hash_file(filename=file2)

            return (
                "\nFile Has been Modified."
                if hash1 != hash2
                else "\nNo Modifications Have been Made."
            )

        except Exception as error:
            return f"\n{str(error)}"

    @staticmethod
    def main() -> None:
        file_path1: Path = Path(input("Enter the file path 1: "))
        file_path2: Path = Path(input("Enter the file path 2: "))

        if not file_path1.exists() or not file_path2.exists():
            print("\nFile(s) not Found.")
            return

        result: str = Integrity.verify_integrity(
            file1=str(file_path1), file2=str(file_path2)
        )

        print(result)


if __name__ == "__main__":
    Integrity.main()
