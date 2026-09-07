from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# ==============================
# 🚀 MISSION COSMOS
# ==============================

console.print(
    Panel.fit(
        "[bold cyan]🚀 MISSION COSMOS 🚀[/bold cyan]\n"
        "[white]Space Mission Planning System[/white]",
        border_style="cyan"
    )
)

# ==============================
# 🛰️ MISSION INPUTS
# ==============================

mission_name = input("Enter mission name: ")
spacecraft = input("Enter spacecraft name: ")
starting_location = input("Enter starting location: ")
destination = input("Enter destination: ")
mission_purpose = input("Enter mission purpose: ")
mission_date = input("Enter mission date: ")
mission_duration = input("Enter mission duration: ")
distance = float(input("Enter distance to destination (km): "))
spacecraft_speed = float(input("Enter your spacecraft speed (km/sec): "))
crew = input("Enter crew information: ")

# ==============================
# ⏱️ TRAVEL TIME CALCULATION
# ==============================

travel_time = distance / spacecraft_speed
travel_days = travel_time / 86400

# ==============================
# 📊 MISSION TABLE
# ==============================

table = Table(
    title="🚀 MISSION COSMOS — MISSION DATA",
    show_header=True,
    header_style="bold cyan"
)

table.add_column("Mission Detail", style="bold green")
table.add_column("Information", style="white")

table.add_row("Mission", mission_name)
table.add_row("Spacecraft", spacecraft)
table.add_row("Starting Location", starting_location)
table.add_row("Destination", destination)
table.add_row("Mission Purpose", mission_purpose)
table.add_row("Mission Date", mission_date)
table.add_row("Mission Duration", mission_duration)
table.add_row("Distance", f"{distance} km")
table.add_row("Spacecraft Speed", f"{spacecraft_speed} km/sec")
table.add_row("Crew", crew)
table.add_row("Travel Time", f"{travel_time:.2f} seconds")
table.add_row("Travel Time in Days", f"{travel_days:.2f} days")

console.print()
console.print(table)

# ==============================
# ✅ MISSION STATUS
# ==============================

console.print()
console.print(
    Panel(
        "[bold green]MISSION DATA CALCULATED SUCCESSFULLY![/bold green]\n"
        "[white]Mission Cosmos is ready for launch planning. 🚀[/white]",
        title="MISSION STATUS",
        border_style="green"
    )
)