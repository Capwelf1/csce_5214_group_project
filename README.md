# CSCE 5214 Group Project: Flight Price Prediction

A Flask web application that estimates flight ticket prices with machine-learning models. This repository is the team's updated version of an existing flight-price prediction application for **CSCE 5214, Software Development for AI**.

**Project repository:** https://github.com/keith44/csce_5214_group_project

## What this version includes

- Four trained model types: **LightGBM, Random Forest, XGBoost, and CatBoost**.
- A **model registry** that stores trained models under versioned folders (`models/v1/`, `models/v2/`, etc.). The application loads whichever version is selected in `models/active_model.json`.
- Model metadata, including the algorithm, training date, features, and validation results.
- A Flask prediction form with flight options based on the training dataset and validation of selected flight combinations.
- **Prediction monitoring** in a local SQLite database, including model version, prediction, response time, and errors.
- A reproducible **Python 3.13** development environment managed with **uv**.

The repository already contains registered model files, so **you do not need to train models just to run the web application**.

---

## Start here if you have never used GitHub or uv

### A few terms

| Term | Meaning |
|---|---|
| **Git** | Software on your computer that tracks changes to files. |
| **GitHub** | A website where Git repositories can be shared and reviewed. |
| **Repository (repo)** | The project and its change history. |
| **Fork** | Your own GitHub copy of this project. You can work on it without changing the team's original repository. |
| **Clone** | Download a GitHub repository onto your computer using Git. |
| **Branch** | A separate line of work where you can make changes without changing `main`. |
| **Commit** | A saved snapshot of your changes in Git. |
| **Push** | Upload your local commits to GitHub. |
| **Pull request (PR)** | Ask the team to review changes from your fork before they become part of the main project. |
| **uv** | The Python tool we use to install the right Python version, create `.venv`, and manage dependencies. |

**Our team workflow:** Fork the repository → clone your fork → create a branch → make changes → test → commit → push → open a pull request. **Do not make changes directly to the team's `main` branch.**

## 1. Install the tools (one time per computer)

The instructions below use **Windows** and a terminal such as **Command Prompt (CMD)**, **PowerShell**, or the VS Code terminal.

### 1A. Create a GitHub account

1. Go to https://github.com and create an account if you do not have one.
2. Sign in to GitHub.
3. Open the team project: https://github.com/keith44/csce_5214_group_project.

### 1B. Install Git

1. Download and install **Git for Windows**: https://git-scm.com/downloads/win.
2. Close and reopen your terminal after installation.
3. Check the installation:

```cmd
git --version
```

You should see a Git version number. If this is your first time using Git, set the name and email associated with your commits (use your own name and the email associated with your GitHub account):

```cmd
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

These commands identify the author of your commits. Replace the examples with your information.

### 1C. Install uv

Open **PowerShell** and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen the terminal, then check:

```cmd
uv --version
```

You should see a uv version number. **You do not need to manually install Python or use Anaconda for this project**. uv can install the required Python version.

Official instructions: https://docs.astral.sh/uv/getting-started/installation/

### 1D. Install VS Code (recommended)

Download VS Code from https://code.visualstudio.com/. Install its **Python** and **Jupyter** extensions if you plan to edit Python files or run the training notebook.

## 2. Fork the team's repository on GitHub

**Do this on the GitHub website, not in the terminal.**

1. Open https://github.com/keith44/csce_5214_group_project.
2. Make sure you are signed in to your own GitHub account.
3. Click **Fork** near the upper-right corner of the repository page.
4. Under **Owner**, select your own GitHub account.
5. Keep the suggested repository name (or choose another name).
6. Leave **Copy the `main` branch only** selected if that option appears.
7. Click **Create fork**.

You should now have a repository at a URL similar to:

```text
https://github.com/YOUR_USERNAME/csce_5214_group_project
```

The project under `keith44` is the **team's repository**. The one under your username is **your fork**. Your changes should be pushed to **your fork**, not directly to the team repository.

Official GitHub instructions: https://docs.github.com/en/get-started/quickstart/fork-a-repo

## 3. Clone your fork onto your computer

1. Open **your fork** on GitHub (`https://github.com/YOUR_USERNAME/csce_5214_group_project`).
2. Click the green **Code** button.
3. Select **HTTPS**, then click the copy icon to copy your fork's URL.
4. Open CMD, PowerShell, or the VS Code terminal.
5. Navigate to the folder where you want to keep your projects. For example:

```cmd
cd %USERPROFILE%\Documents
```

6. Clone **your own fork**, replacing `YOUR_USERNAME`:

```cmd
git clone https://github.com/YOUR_USERNAME/csce_5214_group_project.git
cd csce_5214_group_project
```

**Important:** The URL in `git clone` must contain **your GitHub username**, not `keith44`. If Git asks you to sign in, complete the GitHub authentication prompts. Do **not** paste your GitHub account password into a terminal password prompt; GitHub HTTPS access uses supported authentication methods such as a browser sign-in or token.

To check where your local project will push commits:

```cmd
git remote -v
```

The `origin` URL should point to **your fork**.

## 4. Set up Python and run the Flask application

Open a terminal **inside the cloned `csce_5214_group_project` directory** and run:

```cmd
uv sync
```

This reads `pyproject.toml`, `uv.lock`, and `.python-version`, then creates a local `.venv` and installs the project's dependencies. The project uses **Python 3.13**. The first setup may involve downloading Python and packages.

Verify Python:

```cmd
uv run python --version
```

It should report Python 3.13.x.

Start the application:

```cmd
uv run python app.py
```

Open your browser to:

**http://127.0.0.1:5000**

Choose flight details and submit a prediction. Stop the server with **Ctrl+C** in the terminal.

**You do not need to activate `.venv` manually** when using `uv run`. Use `uv run python ...` instead of plain `python ...` so the program uses the project environment.

### Running the training notebook in VS Code (only if needed)

1. Open the cloned project folder in VS Code (**File → Open Folder**).
2. Open `Flight_Price_Prediction_Training.ipynb`.
3. Click the kernel selector in the upper-right corner.
4. Select the Python interpreter located at `csce_5214_group_project\.venv\Scripts\python.exe` (it might appear under **Python Environments**).
5. Run this notebook cell to check the interpreter:

```python
import sys
print(sys.executable)
```

The printed path should point into the project's `.venv` directory.

If VS Code does not show that interpreter as a kernel, register it from the **project directory**:

```cmd
uv run python -m ipykernel install --user --name flight-price-project --display-name "Python 3.13 (Flight Price Project)"
```

Reload VS Code and select **Python 3.13 (Flight Price Project)**. This kernel registration is specific to your local computer.

## 5. Make changes on a new branch

**Never start your feature by editing `main`.**

Open a terminal in your cloned project and check your branch:

```cmd
git branch
```

Before starting new work, update your fork's `main` branch (see [Section 8](#8-keep-your-fork-up-to-date)) and then create a branch:

```cmd
git switch main
git switch -c feature/describe-your-change
```

Replace `describe-your-change` with a short description, such as:

```cmd
git switch -c feature/improve-error-handling
```

**Run either the example or your own branch name, not both.**

Make your changes in VS Code, save the files, and test the application:

```cmd
uv run python app.py
```

If you change training or model files, test the relevant training/registry steps as well.

## 6. Save and upload your changes

After testing your change, run:

```cmd
git status
```

This shows which files have changed. Review the list. Do not commit `.venv`, the local prediction database, secrets, or unrelated files.

Stage your changes:

```cmd
git add .
```

Save a commit with a clear message:

```cmd
git commit -m "Improve prediction error handling"
```

Upload your branch to **your fork**:

```cmd
git push -u origin feature/improve-error-handling
```

Use your *actual branch name* in the push command if you chose something different. The first push might prompt you to authenticate with GitHub.

**Important:** `git commit` saves changes locally. `git push` uploads them to your fork. **Neither action changes the team's `main` branch.**

## 7. Open a pull request (PR)

A pull request asks to move your finished changes **from your fork into the team's repository**. It does not merge the changes automatically.

1. Go to your fork on GitHub and select the branch you pushed.
2. Click **Contribute → Open pull request**, or click the **Compare & pull request** button if GitHub shows one.
3. Check the branch selection at the top carefully:
   - **Base repository:** `keith44/csce_5214_group_project`
   - **Base branch:** `main`
   - **Head/compare repository:** `YOUR_USERNAME/csce_5214_group_project`
   - **Compare branch:** `feature/improve-error-handling` (or your branch name)
4. Give the pull request a clear title.
5. In the description, explain **what you changed**, **why**, and **how you tested it**. Include screenshots if the user interface changed.
6. Click **Create pull request**.
7. Wait for review. If someone requests changes, edit the same branch on your computer, commit, and push again. The existing pull request updates automatically.

### Example PR description

```text
What changed:
- Added clearer error handling for failed predictions.

Why:
- Users need a useful message if a model cannot make a prediction.

Testing:
- Ran the Flask application with uv.
- Tested a valid prediction and an invalid input.
```

**Only an authorized maintainer can merge into the team repository.** Do not merge your own work unless the team has agreed that you should. Once a pull request is merged, GitHub adds those approved changes to the team's `main` branch.

Official instructions: https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork

## 8. Keep your fork up to date

As the team merges pull requests, your fork can fall behind the team repository. **Before starting each new task:**

1. On GitHub, open **your fork** and select its **`main` branch**.
2. Click **Sync fork → Update branch** to copy the newest changes from the team repository into your fork.
3. Back on your computer, open the terminal in your cloned project and run:

```cmd
git switch main
git pull origin main
uv sync
```

Now create a **new feature branch** from the updated `main`:

```cmd
git switch -c feature/your-next-change
```

**Do not work directly on `main`, and do not force-push to `main`.** If Git reports merge conflicts, ask the team before overwriting files or using `--force`.

Official instructions: https://docs.github.com/en/pull-requests/how-tos/work-with-forks/syncing-a-fork

## 9. Adding or updating dependencies

Use **uv** rather than installing packages manually with `pip` into your Conda or system Python environment.

To add a new dependency, for example:

```cmd
uv add matplotlib
```

This updates **both** `pyproject.toml` and `uv.lock`. Commit those two files as part of your change so everyone gets the same dependency versions after `uv sync`.

To run a Python script in the project environment:

```cmd
uv run python your_script.py
```

Do not commit `.venv`. Each teammate's machine creates its own `.venv` with `uv sync`.

## 10. Model training, registration, and monitoring

### Trained models

`models/` contains the registered models used by the Flask app:

```text
models/
├── active_model.json
├── v1/
│   ├── model.pkl
│   └── metadata.json
├── v2/
│   ├── model.pkl
│   └── metadata.json
├── v3/
│   ├── model.pkl
│   └── metadata.json
└── v4/
    ├── model.pkl
    └── metadata.json
```

**Do not assume that a given version number always corresponds to a particular algorithm.** Open that version's `metadata.json` to see the algorithm and validation metrics. The version numbers depend on the order the models were registered.

To see which version the application uses, open `models/active_model.json`.

To activate a registered model version, run (example: `v1`):

```cmd
uv run python -c "from model_registry import activate_model; activate_model('v1')"
```

To retrain the models, run `Flight_Price_Prediction_Training.ipynb`. Its latest outputs are written to `training/`; that folder is intentionally excluded from Git because the saved model files are registered separately.

After retraining, register new model files:

```cmd
uv run python -c "from model_registry import register_all_models; print(register_all_models())"
```

Then activate the intended version and test it with Flask. **Changes to the tracked `models/` files or `active_model.json` should go through a pull request**, since other teammates will use them too.

### Prediction monitoring

The application writes prediction records to `predictions.db` on your computer. The database can contain timestamps, model versions, predicted prices, response times, and error information. It is ignored by Git, so **your local prediction logs are not shared through GitHub**.

## 11. Project file guide

```text
csce_5214_group_project/
├── app.py                             # Flask application and prediction routes
├── model_registry.py                  # Register, load, and activate model versions
├── prediction_monitor.py              # SQLite prediction logging
├── Flight_Price_Prediction_Training.ipynb
├── train.csv                          # Dataset used for model training and UI options
├── pyproject.toml                     # Python dependency declarations
├── uv.lock                            # Locked dependencies for the team
├── .python-version                    # Python 3.13 selection
├── .gitignore                         # Files not committed to Git
├── models/                            # Registered models + metadata
├── templates/
│   └── home.html                      # Web page
└── static/
    └── css/
        └── styles.css                 # Web page styling
```

`.venv/`, `training/`, and `predictions.db` are local/generated and should not be committed. Do not delete the registered model files under `models/`; the Flask app needs them for predictions.

## 12. Common problems

**`git` is not recognized:** Install Git for Windows, then close and reopen your terminal.

**`uv` is not recognized:** Install uv, then close and reopen your terminal before checking `uv --version` again.

**`ModuleNotFoundError`:** Make sure you are in the project folder and run `uv sync`. Run the app using `uv run python app.py`, not another Python interpreter.

**Jupyter is using Anaconda instead of the project environment:** Select the Python interpreter inside the project's `.venv` as explained in Section 4.

**`Address already in use`:** Another Flask process may still be running on port 5000. Stop the old process before starting another one.

**GitHub rejects your push:** Check `git remote -v`; `origin` should be **your fork**. Make sure you're pushing a **feature branch**, not the team's `main`.

**Your pull request has conflicts:** Your branch may be behind `main` or overlap with another person's changes. Ask for help resolving conflicts before merging.

---

## Repository owner: review and branch protection settings

These steps are for the owner of `keith44/csce_5214_group_project`, **not for teammates setting up their computers**.

**Pull requests do not automatically merge by default.** For stronger protection, set a rule on the team's `main` branch:

1. Open the team repository on GitHub.
2. Select **Settings → Branches → Add classic branch protection rule**.
3. In **Branch name pattern**, enter `main`.
4. Select **Require a pull request before merging**.
5. Select **Require approvals** and set **1 approval**.
6. Optionally select **Do not allow bypassing the above settings** if the owner also wants the rule to apply to administrators. Be aware this can make the owner's own changes require another eligible reviewer.
7. Do **not** enable force pushes or branch deletion.
8. Save the rule.

On **GitHub Free**, branch protection is supported for **public** repositories. Other plan rules apply to private repositories. If the project is public and the team contributes through forks and PRs, teammates **do not need write/collaborator access** to propose changes. Not granting write access also prevents them from directly pushing to the team repository. Granting write access would give people additional permissions, so do so only if needed.

**Review each pull request before merging:** check the changed files, confirm the tests/workflow described in the PR, request changes when necessary, and click **Merge pull request** only when approved. Do not enable automatic merging on a PR unless you intentionally want that behavior.

GitHub documentation: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule

## Attribution

This school project builds on **[Flight-Price-Prediction by Mandal-21](https://github.com/Mandal-21/Flight-Price-Prediction)**, an existing Flask application for predicting flight prices. The team adapted and extended the original project with the features and workflow documented above.
