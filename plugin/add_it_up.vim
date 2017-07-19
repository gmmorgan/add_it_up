" --------------------------------
" Add our plugin to the path
" --------------------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! Additup()
python3 << endOfPython

from add_it_up import add_it_up_example

add_it_up_example()

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! <leader>+ call Additup()
