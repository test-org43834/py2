import example.cli
import example.version

@example.cli.main.command(help="Show the version of the application.")
def version() -> None:
	print(example.version.version())
