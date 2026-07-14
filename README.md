<!--
<p align="center">
  <img src="assets/projectLogo.png" width="200px" alt="Project Logo"/>
</p>-->


<p align="center">
  <em>
    A terminal-based Python script that fully automates updating and managing your Minecraft client-side modpacks using the Modrinth API.
  </em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-00AF5C?style=flat-square&logo=opensourceinitiative&logoColor=white"/>
  <img src="https://img.shields.io/badge/For-Minecraft-00AF5C?style=flat-square&logo=internet-computer&logoColor=white"/>
  <img src="https://img.shields.io/badge/🛠_Status-Developing-00AF5C?style=flat-square"/>
</p>


<p align="center"><em>Built with:</em></p>


<p align="center">

  <img src="https://img.shields.io/badge/Language-Python 3.x-00AF5C?style=flat-square&logo=code&logoColor=white"/>

  <img src="https://img.shields.io/badge/Library-Hashlib-00AF5C?style=flat-square&logo=buffer&logoColor=white"/>
  
  <img src="https://img.shields.io/badge/API-Modrinth-00AF5C?style=flat-square&logo=modrinth&logoColor=white"/>

  <img src="https://img.shields.io/badge/Editor-Vscode-00AF5C?style=flat-square&logo=codepen&logoColor=white"/>
</p>

---


<details><summary><b>📋 Table of Contents</b></summary>

- [🧭 Overview](#overview) 
  - [Why Minecraft Modpack Updater?}](#ㅤ---)
- [⚙️ Features](#features) 
- [📁 Project Structure](#project-structure) 
- [🗂️ Project Index](#project-index) 
- [🧩 Get Started](#get-started) 
  - [🚀 Installation](#Installation) 
  - [🧠 Usage](#usage)
    - [🧭 Execution Flow](#mode-flow) 
- [🌈 Roadmap](#roadmap) 
- [🤝 Contributing](#contributing) 
- [✨ Acknowledgments](#acknowledgments) 
- [💖 Support the developers](#support-the-developers) 
- [📜 License](#license)

</details>


<a id="overview"></a>
## 🧭 Overview

The Minecraft Modpack Updater is a terminal-based Python script designed to fully automate the tedious process of updating client-side modpacks. Leveraging the Modrinth API, the tool transforms a manual, error-prone chore into a seamless, modular, and nearly 100% automated experience directly from your operating system's command line. It handles version scanning, compatibility checks, and file deployment in the background, requiring the user only to manually update their chosen mod loader.


### ㅤ---
<details><summary><b>Why Minecraft Modpack Updater?</b></summary>

Managing Minecraft mods manually is a massive frustration that involves opening dozens of browser tabs, checking individual files for updates, and cross-referencing game version compatibility. This project exists to eliminate that workflow entirely. By handling the heavy lifting through the Modrinth API, it allows players and modpack developers to transition an entire modpack from one Minecraft version to another in a matter of seconds.

What differentiates this tool is its focus on safety, speed, and clear terminal feedback. Before making any changes to your files, the script automatically backs up your current mod configuration into a dedicated folder inside the root directory. This gives users the stability to experiment freely, knowing they can safely downgrade or revert to a previous state at any time simply by running the script again and typing the desired version. Additionally, the built-in tracking alerts you if a mod lacks a stable build for your target patch, or if only alpha/beta releases are available, providing total clarity before you launch the game.

</details>

---


<a id="features"></a> 
## ⚙️ Features

|      | Category          | Description |
| :--- | :---------------- | :----------- |
| 🎯 | **Core Functionality** | Automates client-side modpack updates by fetching compatible files directly from the Modrinth API |
| 🛠️ | **System Structure**   | Modular Python architecture executed entirely through a lightweight and interactive terminal interface |
| 🔍 | **Logging & Debugging** | Scans and alerts the user about mod compatibility, flagging if a mod only has alpha/beta releases available |
| 🛡️ | **Safety & Backup** | Automatically backs up current mods before updating, allowing seamless rollbacks and version downgrades |


---

<!-- Project Structure -->

<a id="project-structure"></a>
## 📁 Project Structure


  ```sh
    minecraft-modpack-updater/
    ├── backupmods/               # Automated local backups directory
    ├── Main                      # Main file where you run the program
    ├── assets                     # Assets stuff
    └── src/                      # Core source code
        ├── api.py                # Modrinth API integration and slug fetching
        ├── core.py               # Main update workflow and download manager
        ├── io_local.py           # File system scanner and JAR metadata extractor
        ├── TerminalController.py # UI/UX text formatting and terminal styling
        └── mods.json             # Local database mapping JARs to Modrinth IDs
  ```

<a id="project-index"></a>
### 🗂️ Project Index
<details open>
    <summary><b>src (Main Module)</b></summary>
    <blockquote>
        <div class='directory-path' style='padding: 8px 0; color: #666;'>
            <code><b>⦿ src</b></code>
        </div>
        <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File</th>
                    <th style='text-align: left; padding: 8px;'>Description</th>
                </tr>
            </thead>
            <tr style='border-bottom: 1px solid #eee;'>
                <td style='padding: 8px;'>
                    <b><a href='./src/core.py'>core.py</a></b>
                </td>
                <td style='padding: 8px;'>
                    - Orchestrates the update verification cycle<br>
                    - Filters game versions and mod loaders compatibility<br>
                    - Downloads updated .jar files directly to the active folder
                </td>
            </tr>
            <tr style='border-bottom: 1px solid #eee;'>
                <td style='padding: 8px;'>
                    <b><a href='./src/api.py'>api.py</a></b>
                </td>
                <td style='padding: 8px;'>
                    - Interfaces with the official Modrinth API<br>
                    - Implements robust validation filters to prevent wrong ID matches<br>
                    - Features dynamic slug manipulation (fixes suffixes, prefix inversion, and forks)
                </td>
            </tr>
            <tr style='border-bottom: 1px solid #eee;'>
                <td style='padding: 8px;'>
                    <b><a href='./src/io_local.py'>io_local.py</a></b>
                </td>
                <td style='padding: 8px;'>
                    - Handles all disk operations (reading/writing database configurations)<br>
                    - Scans the target folder ignoring non-mod assets (like system files)<br>
                    - Parses internal `.jar` structures to extract Fabric IDs
                </td>
            </tr>
            <tr style='border-bottom: 1px solid #eee;'>
                <td style='padding: 8px;'>
                    <b><a href='./src/TerminalController.py'>TerminalController.py</a></b>
                </td>
                <td style='padding: 8px;'>
                    - Manages command-line UI elements, formatting, and colors<br>
                    - Standardizes console outputs, error messages, and success logs
                </td>
            </tr>
            <tr style='border-bottom: 1px solid #eee;'>
                <td style='padding: 8px;'>
                    <b><a href='./src/mods.json'>mods.json</a></b>
                </td>
                <td style='padding: 8px;'>
                    - Persists mapped mod associations as key-value pairs (`JAR_filename: modrinth_id`)
                </td>
            </tr>
        </table>
    </blockquote>
</details>

---

<a id="get-started"></a>
## 🧩 Get Started


To run the Minecraft Modpack Updater, you just need Python installed on your system along with a few external dependencies to handle the terminal interface and API requests.

<a id="Installation"></a>
### 🛠️ Installation & Setup

<details open>
<summary><b>Show installation steps</b></summary>

#### **1. Clone the repository**
```bash
git clone https://github.com/Turzimmgit/minecraft-modpack-updater.git
cd minecraft-modpack-updater
```
<!--
#### **2. Install dependencies**

```bash
pip install -r requirements.txt
```

#### **3. Configure environment variables**


```env
API_KEY=your_api_key_here
DB_URL=your_database_url_here
```
-->
#### **2. Run the project**

```bash
python Main.py
```

---

<a id="usage"></a>
### 🧠 Usage

The script is entirely interactive and runs straight inside your operating system's command line. You do not need to configure complex environment files or manage permissions.



<a id="mode-flow"></a>
#### 🧭 Execution flow

The tool processes your folders sequentially to secure your files and keep you informed. First, launch the script in your terminal. When prompted, type the target Minecraft version you want to update your modpack to (for example, 1.21.4).

The script will instantly create a safety copy of your current files inside the backupmods/ directory. After securing your files, it fetches the Modrinth API data, checks for available updates, and displays a clear summary in the terminal. If a mod only has alpha or beta builds available, the script flags it to let you know before finalizing the downloads.

If anything goes wrong or if you simply want to downgrade later, just run the script again and type your previous game version to trigger a rolling back process using your saved backups.

---
</details>

<a id="roadmap"></a>
## 🌈 Roadmap


- [X] Modrinth API Integration: Connect and dynamically fetch metadata structures from the official endpoint.

- [X] Automated Local Backups: Create zip/folder state copies inside backupmods/ before executing modifications.

- [/] Mod Loader Validation: Implement guided checkups to alert users if their Fabric, Forge, or NeoForge loaders need manual updates.

- [X] Automated Mod Downloading: Extract file URLs from payload and download the updated `.jar` files directly

- [ ] Dependency Resolution: Automatically detect and download core library mods required by your main mods.

- [ ] Multi-Profile Support: Manage independent mod folders or different game instances from a single script configuration support.

---

<a id="contributing"></a>
## 🤝 Contributing


- **💬 [Open Discussions](https://github.com/turzimmgit/minecraft-modpack-updater/discussions):** Share insights, provide feedback, or ask questions  
- **🐛 [Report Issues](https://github.com/turzimmgit/minecraft-modpack-updater/issues):** Submit bugs you find or request new features  
- **💡 [Send Pull Requests](https://github.com/turzimmgit/minecraft-modpack-updater/pulls):** Review open PRs and send your contributions  
<details closed>
<summary>Contribution Guidelines</summary>


1. **Fork the Repository**
   Make a personal copy of the project on your Git hosting platform.

2. **Clone the Fork Locally**

   
   ```sh
   git clone https://github.com/turzimmgit/minecraft-modpack-updater
   ```
   
3. **Create a New Branch**

   
   ```sh
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   Implement, document, and test modifications locally.

5. **Commit Your Changes**

   
   ```sh
   git commit -m "Short description of the update"
   ```

6. **Push to GitHub**

   ```sh
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   Submit the PR to the main repository, explaining the purpose and details of your changes.

8. **Review & Merge**
   After review and approval, the contribution is merged into the main branch.

</details>

---

<a id="acknowledgments"></a>
## ✨ Acknowledgments

This project is built on the shoulders of giants, and its development wouldn't be possible without the incredible tools and communities that support the open-source ecosystem.

A special thanks goes to Modrinth for providing a powerful, stable, and well-documented API that makes automated mod management possible. This project also owes its foundation to the Python community and the creators of the core libraries used throughout the script, which allowed for a clean and modular terminal interface. Finally, a huge thank you to the developer communities for sharing knowledge, the testers who helped validate early versions of the script, and every player whose feedback keeps this tool evolving and improving.

---

<a id="support-the-developers"></a>
## 💖 Support the developers
Thank you for using the Minecraft Modpack Updater! This project was built to solve a personal frustration, and seeing it help others save time, streamline their workflows, and keep their games up to date is incredibly rewarding.

If this script has made your modding life easier, inspired your own projects, or saved you from the nightmare of opening dozens of browser tabs, please consider leaving a ⭐ on GitHub. Starring the repository takes just a second, but it goes a long way in increasing the project's visibility, helping other players find it, and fueling its growth.

You can also follow the project's development to stay updated on new releases, bug fixes, and future improvements. Every single form of support—whether it is a star, a follow, sharing the project with your friends, or opening an issue with constructive feedback—plays a massive role in keeping this project active, polished, and constantly evolving. Your support means the world!

* **Artur Ferreira — Project Owner & Lead Developer**  
📎 https://github.com/Turzimmgit

---

<a id="license"></a>
## 📜 License

This project is licensed under the **MIT**.
For full details, see the [LICENSE](https://github.com/TurzimmGit/minecraft-modpack-updater/blob/main/LICENSE) file.

<p align="left">
  <a href="#top">
    <img src="https://img.shields.io/badge/Back_to_Top_⭱-00AF5C?style=flat&logoColor=white" />
  </a>
</p>
