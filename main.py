import click
import json

from writers.statistics_m1 import StatisticsModule1


MODULES = {"statistics_m1": StatisticsModule1}


@click.command()
@click.option(
    "--module",
    "-m",
    default="all",
    help="keyword to select the module to be written. See repo list.",
    show_default=True,
)
@click.version_option(version="0.0.1")
def main(module: str):
    """Generates documents using writers modules.

    Args:
        module (str): keyword to select the module to be written. Defaults to 'all'
    """

    assert module in MODULES or module == "all", f"There are no module named {module}"

    click.echo("===== 📝 Random Teacher =====")
    with open("conf.json", "r") as file:
        conf = json.load(file)

    if module == "all":
        click.echo("\tAll available modules are going to be generated.")
        for key, WriterClass in MODULES.items():
            click.echo(f"\tCreating module {key}.")
            writer = WriterClass(conf)
            writer.write()
            print("\t-------------------------------------")
        click.echo("\tAll modules were created succesfully.")
    else:
        click.echo(f"\tCreating module {module}.")
        writer = MODULES[module](conf)
        writer.write()
        click.echo("\tThe module was created succesfully.")


if __name__ == "__main__":
    main()
