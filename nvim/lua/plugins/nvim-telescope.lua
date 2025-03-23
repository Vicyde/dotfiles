return {
  "nvim-telescope/telescope.nvim",
  branch = '0.1.x',
  dependencies = { 
    "nvim-lua/plenary.nvim",
    "nvim-tree/nvim-web-devicons",
  },
  config = function()
    local telescope = require("telescope")
    local actions = require("telescope.actions")
    local km = vim.keymap

    telescope.setup({ 
      defaults = {
        mappings = { 
          i = { 
            ["<C-k>"] = actions.move_selection_previous,
            ["<C-j>"] = actions.move_selection_next,
          }
        }
      }
    })
    km.set("n", "<leader>ff", "<cmd>Telescope find_files<cr>", { desc = "Fuzzy find files" })
    km.set("n", "<leader>fr", "<cmd>Telescope oldfiles<cr>", { desc = "Fuzzy find in recentfiles" })
    km.set("n", "<leader>fs", "<cmd>Telescope live_grep<cr>", { desc = "Find string" })
    km.set("n", "<leader>fc", "<cmd>Telescope grep_string<cr>", { desc = "Find string under cursor" })
  end,
}
