return {
  "sainnhe/everforest",
  priority=1000,
  lazy=false,
  config = function()
    vim.opt.background = 'dark' 
    vim.g.everforest_enable_italic = true
    vim.g.everforest_background = 'hard'
    vim.cmd("colorscheme everforest")
  end,
}
