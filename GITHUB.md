# Review Hotmouse Plus Overview - GitHub Repository

This repository contains the source code for the **Review Hotmouse Plus Overview** Anki add-on.

## Quick Links

- **Main Repository**: [https://github.com/athulkrishna2015/Review-Hotmouse-Plus-Overview/](https://github.com/athulkrishna2015/Review-Hotmouse-Plus-Overview/)
- **Install via AnkiWeb**: [Add-on ID 1054369752](https://ankiweb.net/shared/info/1054369752)
- **Report an Issue**: [Issues Page](https://github.com/athulkrishna2015/Review-Hotmouse-Plus-Overview/issues)
- **Latest Releases**: [Releases Page](https://github.com/athulkrishna2015/Review-Hotmouse-Plus-Overview/releases)

## Development & Contribution

### Local Testing (Symlinking)

The fastest way to test your changes is to symlink the `addon/` folder directly into your Anki add-ons directory. This way, any code changes are picked up immediately after restarting Anki.

**On Linux (Standard):**
```shell
ln -s "$(pwd)/addon" "~/.local/share/Anki2/addons21/review_hotmouse_dev"
```

**On Windows (PowerShell as Admin):**
```powershell
New-Item -ItemType SymbolicLink -Path "$env:APPDATA\Anki2\addons21\review_hotmouse_dev" -Target "$pwd\addon"
```

### Building the `.ankiaddon` file

To bundle the addon for manual installation, run the following command in the project root:

```shell
python make_ankiaddon.py
```

This will generate a timestamped file like `Review_Hotmouse_Plus_Overview_YYYYMMDDHHMM.ankiaddon`.

### Formatting & Type Checking

We use [black] for formatting and [mypy] for static type analysis to maintain code quality.

```shell
# Format the code
black .

# Check for type errors
mypy .
```

### Environment Setup

You will need the following Python packages for development:

```shell
pip install aqt PyQt6 mypy black
```

## How to Contribute

1. **Fork the Repository**: Create your own copy of the project.
2. **Make Changes**: Implement your features or bug fixes.
3. **Verify**: Run the formatting and type checks mentioned above.
4. **Submit a Pull Request**: Explain your changes and why they are beneficial.

---

*This project is a fork of the original [Review Hotmouse](https://github.com/BlueGreenMagick/Review-Hotmouse/) by BlueGreenMagick.*
