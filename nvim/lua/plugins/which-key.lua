return {
  "folke/which-key.nvim",
  event = "VeryLazy",
  config  = function() 
    local wk = require('which-key')

    wk.register({ 
      ["<leader>"] = {
        e = { name="Explorer" },
        s = { name="Split" },
        t = { name="Tab" },
        f = { name="Fuzzy" },
      }
    })
  end,
  init = function() 
    vim.o.timeout = true
    vim.o.timeoutlen = 500
  end,
  opts = {

  },
}
