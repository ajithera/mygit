
# 🚀 GitHub Multi-Account Setup Guide (acc_1 & acc_2)

This guide helps you manage **two GitHub accounts** on the same local machine (acc_1 and acc_2), ensuring that the correct identity and SSH key are used per project.

---

## 🔑 1. Generate SSH Keys

```bash
# acc_1 account key
ssh-keygen -t ed25519 -C "mail_1@gmail.com" -f ~/.ssh/id_ed25519_acc_1

# acc_2 account key
ssh-keygen -t ed25519 -C "mail_2@gmail.com" -f ~/.ssh/id_ed25519_acc_2
```

Add each public key to the respective GitHub account:
- acc_1: `~/.ssh/id_ed25519_acc_1.pub`
- acc_2: `~/.ssh/id_ed25519_acc_2.pub`

---

## ⚙️ 2. SSH Config Setup

Edit (or create) the SSH config file:

```bash
nano ~/.ssh/config
```

Add the following:

```ssh
# acc_1 GitHub account
Host github.com-acc_1
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_acc_1
  IdentitiesOnly yes

# acc_2 GitHub account
Host github.com-acc_2
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_acc_2
  IdentitiesOnly yes
```

---

## 📦 3. Clone Repositories with Custom Hosts

### acc_1 Repository

```bash
git clone git@github.com-acc_1:acc_1/repo1.git
```

### acc_2 Repository

```bash
git clone git@github.com-acc_2:repo2.git
```

---

## 👤 4. Set Local Git Identity per Repository

### For acc_1 Repo

```bash
cd projects
git config user.name "acc_1"
git config user.email "mail_1@gmail.com"
```

### For acc_2 Repo

```bash
cd gcp
git config user.name "acc_2"
git config user.email "mail_2@gmail.com"
```

> ❗ Don't set `--global` here. We want the identity to be repo-specific.

---

## ✅ Verification

Run this in any repo to verify correct identity:

```bash
git config user.name
git config user.email
```

You can also check which SSH key is being used:

```bash
ssh -T git@github.com-acc_1
ssh -T git@github.com-acc_2
```

---

## 🧪 Optional: Shell Script to Automate All Steps

Create a script (e.g., `setup_git_repos.sh`) to clone and configure:

```bash
#!/bin/bash

git clone git@github.com-acc_1:acc_1/repo1.git
cd projects
git config user.name "acc_1"
git config user.email "mail_1@gmail.com"
cd ..

git clone git@github.com-acc_2:repo2.git
cd gcp
git config user.name "acc_2"
git config user.email "mail_2@gmail.com"
cd ..
```

Make it executable:

```bash
chmod +x setup_git_repos.sh
./setup_git_repos.sh
```

---

## 📌 Summary

| Account   | Email                   | SSH Host Alias     | Repo Example                                         |
|-----------|-------------------------|---------------------|------------------------------------------------------|
| acc_1  | mail_1@gmail.com    | `github.com-acc_1` | `git@github.com-acc_1:acc_1/repo1.git`     |
| acc_2      | mail_2@gmail.com    | `github.com-acc_2`     | `git@github.com-acc_2:repo2.git`            |

---

Happy Coding! 💻✨
