return {
  "folke/which-key.nvim",
  event = "VeryLazy",
  config = function()
    local wk = require('which-key')
    wk.add({
      { "<leader>e", name="Explorer" },
      { "<leader>s", name="Split" },
      { "<leader>t", name="Tab" },
      { "<leader>f", name="Fuzzy" },
    })
  end,
  opts = {

  },
}
