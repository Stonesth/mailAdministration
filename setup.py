from cx_Freeze import setup, Executable


setup(
    name = "mailadministration",
    version = "0.1",
    description = "",
    executables = [Executable("mailadministration.py")]
)
