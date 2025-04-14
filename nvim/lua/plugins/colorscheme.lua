return {
  "sainnhe/everforest",
  priority=1000,
  lazy=false,
  config = function()
    vim.g.everforest_enable_italic = true
    vim.cmd("colorscheme everforest")
  end,
}
