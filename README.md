# Orim2016

	
You can run easy_install to install python packages in your home directory even without root access. There's a standard way to do this using site.USER_BASE which defaults to something like $HOME/.local or $HOME/Library/Python/2.7/bin and is included by default on the PYTHONPATH

To do this, create a .pydistutils.cfg in your home directory:

cat > $HOME/.pydistutils.cfg <<EOF
[install]
user=1
EOF

easy_install beautiful soup


./download.sh
