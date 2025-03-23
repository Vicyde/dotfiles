local km = vim.keymap

vim.g.mapleader = " "

km.set("i", "jk", "<ESC>", { desc="Cancel insert mode" })
km.set("i", "jj", "<ESC>", { desc="Cancel insert mode" })

km.set("n", "<leader>sv", "<C-w>v", { desc="Split vertically" })
km.set("n", "<leader>sh", "<C-w>s", { desc="Split horizontally" })
km.set("n", "<leader>se", "<C-w>=", { desc="Make splits equal" })
km.set("n", "<leader>sx", "<CMD>close<CR>", { desc="Close split" })

km.set("n", "<leader>to", "<CMD>tabnew<CR>", { desc="Open a new tab" })
km.set("n", "<leader>tx", "<CMD>tabclose<CR>", { desc="Close the tab" })
km.set("n", "<leader>tn", "<CMD>tabn<CR>", { desc="Next tab" })
km.set("n", "<leader>tp", "<CMD>tabp<CR>", { desc="Previous tab" })
km.set("n", "<leader>tf", "<CMD>tabnew %<CR>", { desc="Open current file in new tab" })

