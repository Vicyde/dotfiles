return {
  "scottmckendry/cyberdream.nvim",
  priority=1000,
  lazy=false,
  config = function()
    require("cyberdream").setup({
      transparent = false,
    })

    vim.cmd("colorscheme cyberdream")
  end,
}
