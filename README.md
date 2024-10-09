# DearPyGui_ThemeLoaders
DearPyGui_ThemeLoader (dpgtl) is an easy way to load and write DearPyGui themes with JSON files.
It comes pre-installed with different example themes

<p align="center">
  <a href="https://github.com/catppuccin/catppuccin">Catppuccin</a>
</p>
<table width="100%">
  <tr>
    <th>Latte</th>
    <th>Frappé</th>
  </tr>
  <tr>
    <td width="10%">
      <img src="https://github.com/user-attachments/assets/da78145b-fd9c-4268-874a-9541ff1b8884" />
    </td>
    <td width="10%">
      <img src="https://github.com/user-attachments/assets/64a5fd6b-5d77-4ab8-91c6-278ca014d5fd" />
    </td>
  </tr>
  <tr>
    <th>Macchiato</th>
    <th>Mocha</th>
  </tr>
  <tr>
    <td width="10%">
      <img src="https://github.com/user-attachments/assets/fdb5689f-dcc9-4c66-9d7c-99aedc64b838" />
    </td>
    <td width="10%">
      <img src="https://github.com/user-attachments/assets/eb3d625d-06a9-45dd-ba75-0344db16c77a" />
    </td>
  </tr>
</table>

### Others
#### [Tokyo Night](https://github.com/folke/tokyonight.nvim)
![python_nqZLS3fCbw](https://github.com/user-attachments/assets/4ecde145-63b5-4528-99f9-73a75154909d)


# Usage
1. Copy dpgtl repository to your project
2. Import `dpgtl.py` to your script, E.g: ```import dpgtl as dpgtl```
3. Use `load_json_theme` function to specify a JSON file where the theme is at, E.g: ```dpgtl.load_json_theme("path/to/theme")```

# Basic JSON theme
Random strange theme
```json
{
    "mvAll": {
        "mvStyleVar_PopupBorderSize": 0,
        "mvStyleVar_ChildBorderSize": 0,
        "mvStyleVar_WindowBorderSize": 10,

        "mvStyleVar_WindowRounding": 10,
        "mvStyleVar_ChildRounding": 3,
        "mvStyleVar_FrameRounding": 3,
        "mvStyleVar_PopupRounding": 3,
        "mvStyleVar_GrabRounding": 0,
        "mvStyleVar_TabRounding": 100,

        "mvStyleVar_WindowTitleAlign": [1, 0],

        "mvThemeCol_WindowBg": [50,198,125,55],
        "mvThemeCol_TitleBg": [199,120,0,50],
        "mvThemeCol_TitleBgActive": [19,120,0,50],
        "mvThemeCol_TitleBgCollapsed": [0,0,0,50],
        "mvThemeCol_MenuBarBg": [0,0,0,100],
        "mvThemeCol_PopupBg": [0,0,0,120],
        "mvThemeCol_ChildBg": [0,0,0,170]
    }
}
```
