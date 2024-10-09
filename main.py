import dearpygui.dearpygui as dpg
import dpgtl as dpgtl

dpg.create_context()

def_t = "themes/json/tokyo-night/tokyo-night.json"

dpg.bind_theme(dpgtl.load_json_theme(def_t))

def link_callback(sender, app_data):
    dpg.add_node_link(app_data[0], app_data[1], parent=sender)

def delink_callback(sender, app_data):
    dpg.delete_item(app_data)

def refresh_theme():
    dpg.bind_theme(dpgtl.load_json_theme(dpg.get_value("def_t")))

with dpg.window(label="Tutorial", width=400, height=400):
    with dpg.tab_bar():
        with dpg.tab(label="data.sav"):
            with dpg.table(borders_innerH=True, borders_innerV=True, borders_outerH=True, borders_outerV=
                           True):
                dpg.add_table_column(label="Year")
                dpg.add_table_column(label="GDP (billions of $)")
                dpg.add_table_column(label="Unemployment rate (%)")

                with dpg.table_row():
                    dpg.add_text("2020")
                    dpg.add_text("2021")
                    dpg.add_text("2022")
                
                with dpg.table_row():
                    dpg.add_text("2000")
                    dpg.add_text("2100")
                    dpg.add_text("2200")

                with dpg.table_row():
                    dpg.add_text("9.3")
                    dpg.add_text("9.0")
                    dpg.add_text("8.5")
            with dpg.child_window():
                dpg.add_text("Gross domestic product\n\nGross domestic product (GDP) is a monetary measure of the market\nvalue of all the final goods and services produced\nand rendered in a specific time period by a country or countries.\nGDP is often used to measure the economic health of a country or region.\nDefinitions of GDP are maintained by several national\nand international economic organizations, such as the OECD and the International Monetary Fund.")
        with dpg.tab(label="data.sav"):
            with dpg.table(borders_innerH=True, borders_innerV=True, borders_outerH=True, borders_outerV=
                           True):

                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                for i in range(0, 4):
                    with dpg.table_row():
                        for j in range(0, 3):
                            dpg.add_text(f"Row{i} Column{j}")

with dpg.window(label="Tutorial", pos=(20, 50), width=275, height=225) as win1:
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="New file...")
            dpg.add_menu_item(label="Open file...")
            dpg.add_separator()
            dpg.add_menu_item(label="New folder...")
            dpg.add_menu_item(label="Open folder...")
            dpg.add_separator()
            with dpg.menu(label="Open recents..."):
                dpg.add_menu_item(label="fsadfa.txt")
                dpg.add_menu_item(label="fsadfa.txt")
                dpg.add_menu_item(label="fsadfa.txt")
                dpg.add_menu_item(label="fsadfa.txt")
                dpg.add_menu_item(label="fsadfa.txt")
                dpg.add_menu_item(label="fsadfa.txt")
                dpg.add_menu_item(label="fsadfa.txt")
                dpg.add_menu_item(label="fsadfa.txt")
                dpg.add_menu_item(label="fsadfa.txt")

                
            dpg.add_separator()
            dpg.add_menu_item(label="Save...")
            dpg.add_menu_item(label="Save as...")
            dpg.add_menu_item(label="Save all...")
        with dpg.menu(label="System"):
            dpg.add_menu_item(label="Exit", shortcut="ALT + F4")
        with dpg.menu(label="Run/Debug"):
            dpg.add_menu_item(label="Run with debugger", shortcut="F5")
            dpg.add_menu_item(label="Run without debugger", shortcut="ALT + F5")
            dpg.add_separator()
            dpg.add_menu_item(label="Add new build system...")
            dpg.add_menu_item(label="Clear build files")
            
        with dpg.menu(label="?"): 
            dpg.add_menu_item(label="About DearPyGui_ThemeLoader")
            dpg.add_menu_item(label="Check for updates...")
            dpg.add_menu_item(label="It lives with sad & happines...")


    dpg.add_input_text(hint="theme.json here", tag="def_t", default_value="themes/json")
    dpg.add_button(label="Refresh theme", callback=refresh_theme)
    t1 = dpg.add_input_text(default_value="some text")
    t2 = dpg.add_input_text(default_value="some text")
    with dpg.child_window(height=100):
        t3 = dpg.add_input_text(default_value="some text")
        dpg.add_input_int()
    dpg.add_input_text(default_value="some text")


print(dpgtl.load_json_theme(def_t))
dpg.show_style_editor()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()