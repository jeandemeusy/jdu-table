from jdutable.tableWriter import TableWriter


def main():
    header = ["Date", "Description", "Amount"]

    data = [
        ["1/1/2014", "Domain name", "$10.98"],
        ["1/1/2014", "January Hosting", "$54.95"],
        ["1/4/2014", "February Hosting", "$51.00"],
        ["1/4/2014", "February Extra Bandwidth", "$30.00"],
    ]

    footer = ["", "Total", "$146.93"]

    table = TableWriter()
    table.set_header(header)
    table.set_footer(footer)

    table.set_uppercased(False)
    table.set_border(True)
    table.set_alignment(["<", "<", ">"])
    table.set_center_separator("")
    table.set_column_separator("!")

    table.append_bulk(data)
    table.render()


if __name__ == "__main__":
    main()
