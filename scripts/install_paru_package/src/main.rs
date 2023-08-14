use dialoguer::{Confirm, MultiSelect};
use std::process::Command;

fn main() {
    let package_names: &[&str] = &[
        "ani-cli",
        "bat",
        "bluetuith",
        "bottom",
        "bleachbit",
        "brightnessctl",
        "cava",
        "dust",
        "firefox",
        "gitoxide",
        "gdu",
        "gparted",
        "htop",
        "lf",
        "kitty",
        "lobster",
        "mako",
        "nano",
        "neofetch",
        "newm-atha-git",
        "nushell",
        "nvtop",
        "mpv",
        "muc-git",
        "imv",
        "onefetch",
        "poweralertd",
        "pulsemixer",
        "python-pywal",
        "redqu",
        "shotman",
        "timeshift",
        "tty-clock-git",
        "ueberzugpp",
        "volumectl",
        "waybar",
        "ytfzf",
        "yt-dlp",
        "zoxide",
    ];
    // Replace with the package names you want to install

    let selected_packages = MultiSelect::new()
        .with_prompt("Select packages to install")
        .items(&package_names)
        .interact()
        .expect("Failed to display package selection");

    let confirmed = Confirm::new()
        .with_prompt("Are you sure you want to install the selected packages ?")
        .interact()
        .expect("Failed to display confirmation prompt");

    if confirmed {
        for &index in &selected_packages {
            let package_name = package_names[index];
            let output = Command::new("paru")
                .arg("-S")
                .arg("--noconfirm") // Optional: Skip confirmation prompts
                .arg("--batchinstall") // Run in batch mode
                .arg(package_name)
                .output()
                .expect("Failed to execute paru command");

            if output.status.success() {
                println!("Package {} installed successfully", package_name);
            } else {
                let error_message = String::from_utf8_lossy(&output.stderr);
                println!(
                    "Failed to install package {}: {}",
                    package_name, error_message
                );
            }
        }
    } else {
        println!("Installation canceled");
    }
}
