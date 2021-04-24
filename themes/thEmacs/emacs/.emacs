; Configuration GNU Emacs 20.5.1 (02/2000)
;; Version : 1.0.0 (06/2000)
;; Philippe ROY <ph_roy@yahoo.com>


;; Receptacle
(custom-set-variables
)

;; Clavier
(custom-set-variables
 '(pc-selection-mode t nil (pc-select)))
(global-set-key "\C-k" 'kill-this-buffer)
(global-set-key "\C-b" 'switch-to-buffer)
(global-set-key "\M-q" 'other-window)
(global-set-key "\C-0" 'delete-window)
(global-set-key "\C-1" 'delete-other-windows)
(global-set-key "\C-x=" 'goto-line)
(global-set-key "\C-g" 'grep)
(global-set-key "\C-e" 'save-buffer)
(global-unset-key [insert])

;; Francais
(iso-accents-mode t)
(require 'iso-insert)
(standard-display-european 1)
(set-input-mode nil nil 1)
(setq ispell-dictionary "francais")

;; Mode : Tex
(global-set-key "\C-t" 'tex-buffer)
;;'(tex-dvi-view-command "xdvi" t)

;; Mode : Sgml
(require 'sgml-mode)
;;(setq sgml-indent-data t)
;;(setq sgml-set-face t)
;;(setq sgml-validate-command "nsgmls -s")
;;(setq sgml-name-8bit-mode nil)

;; Mode : C
(global-set-key "\C-z" 'compile)
(global-set-key "\C-d" 'gdb)

;; Fichier : Definition des modes
(setq auto-mode-alist
      '( 
        ("\\.txt$" . text-mode)
        ("\\.log$" . text-mode)
        ("\\.fsfdb$" . text-mode)
        ("\\README$" . text-mode)
        ("\\AUTHORS$" . text-mode)
        ("\\NEWS$" . text-mode)
        ("\\TODO$" . text-mode)
        ("\\ChangeLog$" . change-log-mode)
        ("\\.am$" . makefile-mode)
        ("\\.c$"  . c-mode) 
        ("\\.h$"  . c-mode)
        ("\\.C$"  . c++-mode) 
        ("\\.cc$" . c++-mode) 
        ("\\.sgml$" . sgml-mode)
        ("\\.xml$" . sgml-mode)
        ("\\.xsl$" . sgml-mode)
        ("\\.dtd$" . sgml-mode)
        ("\\.toutdoux$" . sgml-mode)
        ("\\.hopla$" . sgml-mode)
        ("\\.tex$" . latex-mode )
        ("\\.cls$" . latex-mode )
        ("\\.html$" . html-mode)
        ("\\.shtml$" . html-mode)
        ("\\.php3$" . html-mode)
        ("\\.phtml$" . html-mode)
	("\\.sh$" . sh-mode )
        ("\\.scm$" . scheme-mode) 
        ("\\.l$" . lisp-mode) 
        ("\\.lisp$" . lisp-mode) 
        ("\\.f$" . fortran-mode) 
        ("\\.awk$" . awk-mode )
        ("\\.pl$" . perl-mode )
        ("\\.el$" . emacs-lisp-mode) 
        ("\\.emacs$" . emacs-lisp-mode) 
        ("\\.gnus$" . emacs-lisp-mode))
)

;; Fichier : Speedbar
(custom-set-variables
 '(speedbar-supported-extension-expressions (quote ("\\.vhdl?\\'" 
						    ".emacs"
						    ".cvsignore"
						    ".p" 
						    ".am"
						    ".in"
						    ".spec"
						    ".fsfdb"
						    "README"
						    "AUTHORS"
						    "NEWS"
						    "TODO"
						    "HACKING"
						    "ChangeLog"
						    ".po"
						    ".dat"
						    ".sgml"
						    ".xml"
						    ".xsl"
						    ".dtd"
						    ".html"
						    ".css"
						    ".tex"
						    ".cls"
						    ".c" 
						    ".h" 
						    ".xpm" 
						    ".png" 
						    ".jpeg" 
						    ".gif" 
						    ".toutdoux"
						    ".hopla"
						    ".gnumeric"
						    ".log"
						    ".txt"
						    ".sh"
						    ))))


;; Ecran
(custom-set-variables
 '(visible-bell t)
 '(fill-column 100)
 (hscroll-global-mode t))
(setq line-number-mode t)
(setq column-number-mode t)

;; Colorisation : Generalite
(custom-set-variables
 '(show-paren-style (quote parenthesis))
 '(show-paren-mode t nil (paren))
 '(font-lock-global-modes t)
 '(global-font-lock-mode t nil (font-lock)))
(setq font-lock-maximum-decoration t)


;; Colorisation : Dans ta face PaleGreen
(custom-set-faces
 '(default ((t (:foreground "Wheat" :background "DarkSlateGray"))))
 '(custom-variable-tag-face ((t (:underline t :foreground "LightBlue"))))
 '(speedbar-button-face ((t (:foreground "Wheat"))))
 '(underline ((t (:underline t))))
 '(speedbar-directory-face ((t (:foreground "PaleGreen"))))
 '(speedbar-file-face ((t (:foreground "LightSalmon"))))
 '(region ((t (:foreground "#102829" :background "#6a997b"))))
 '(vc-default-back-end (quote RCS))
 '(custom-saved-face ((t (:underline t :background "DarkSlateGray"))))
 '(font-lock-constant-face ((t (:foreground "LightGoldenrod"))))
 '(speedbar-highlight-face ((t (:foreground "Wheat" :background "DarkOliveGreen"))))
 '(modeline ((t (:inverse-video t :foreground "Tan" :background "DarkSlateGray"))))
 '(show-paren-match-face ((t (:background "IndianRed"))))
 '(font-lock-variable-name-face ((t (:foreground "Aquamarine"))))
 '(speedbar-tag-face ((t (:foreground "LightGoldenrod"))))
 '(bold ((t (:foreground "LightSalmon"))))
 '(speedbar-selected-face ((t (:underline t :foreground "OrangeRed"))))
 '(font-lock-builtin-face ((t (:foreground "Pink"))))
)

;; Colorisation : C : Grands classiks
(font-lock-add-keywords 'c-mode
			'(
			  ("\\<\\(printf\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(getc\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(strtok\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(strcmp\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(strlen\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(atoi\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(fgets\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(fprintf\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(remove\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(rename\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(stat\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(open\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(opendir\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(closedir\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(fstat\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(fopen\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(freopen\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(fclose\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(fflush\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(fpurge\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(feof\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(dlopen\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(dlsym\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(dlerror()\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(sleep;?\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(setenv;?\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(pthread_[-.a-z0-9_]*;?\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(sem_[-.a-z0-9_]*;?\\)\\>" . font-lock-keyword-face)
			  ))

;; Colorisation : C : Commentaires
(font-lock-add-keywords 'c-mode
			'(
			  ("\\<\\(FIXME\\):" 1 font-lock-warning-face prepend)
			  ))

;; Colorisation : C : Xml PostgreSQL
(font-lock-add-keywords 'c-mode
			'(
			  ("\\<\\(xmlNewDoc\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlNewDocNode\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlSetDocCompressMode\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlFreeDoc\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlSaveFile\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlParseFile\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlNewGlobalNs\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlSearchNsByHref\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlNewChild\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlGetProp\\)\\>" . font-lock-constant-face)
			  ("\\<\\(xmlSetProp\\)\\>" . font-lock-constant-face)
			  ("\\<\\(PQsetdbLogin\\)\\>" . font-lock-constant-face)
			  ("\\<\\(PQfinish\\)\\>" . font-lock-constant-face)
			  ("\\<\\(PQexec\\)\\>" . font-lock-constant-face)
			  ("\\<\\(PQresultStatus\\)\\>" . font-lock-constant-face)
			  ("\\<\\(PQnfields\\)\\>" . font-lock-constant-face)
			  ("\\<\\(PQfname\\)\\>" . font-lock-constant-face)
			  ("\\<\\(PQntuples\\)\\>" . font-lock-constant-face)
			  ("\\<\\(PQgetvalue\\)\\>" . font-lock-constant-face)
			  ("\\<\\(PQstatus\\)\\>" . font-lock-constant-face)
			  ))

;; Colorisation : Glib Gdk Gtk+ GNOME
(font-lock-add-keywords 'c-mode
			'(
			  ("\\<\\(g_[-.a-z0-9_]*;?\\)\\>" . font-lock-keyword-face)
			  ("\\<\\(gdk_[-.a-z0-9_]*;?\\)\\>" . font-lock-constant-face)
			  ("\\<\\(gtk_[-.a-z0-9_]*;?\\)\\>" . font-lock-constant-face)
			  ("\\<\\(gnome_[-.a-z0-9_]*;?\\)\\>" . font-lock-constant-face)
			  ("\\<\\(poptGetArgs\\)\\>" . font-lock-constant-face)
			  ))

;; Colorisation : ToutDoux hOpla
(font-lock-add-keywords 'c-mode
			'(
			  ("\\<\\(td_[-.a-z0-9_]*;?\\)\\>" . font-lock-builtin-face)
			  ("\\<\\(hopla_[-.a-z0-9_]*;?\\)\\>" . font-lock-builtin-face)
			  ))


;; Colorisation : Types
(custom-set-variables
 '(c-font-lock-extra-types (quote ("DIR" 
				   "FILE" 
				   "gchar"
				   "gint"
				   "guint"
				   "guint8"
				   "guint32"
				   "gboolean"
				   "gpointer"
				   "GList" 
				   "GSList" 
				   "xmlDocPtr"
				   "xmlNsPtr"
				   "xmlNodePtr"
				   "xmlChar"
				   "PGconn"
				   "PGresult"
				   "pthread_t"
				   "\\<\\(Gdk[-.a-zA-Z0-9_]*;?\\)\\>"
				   "\\<\\(Gtk[-.a-zA-Z0-9_]*;?\\)\\>"
				   "\\<\\(Gnome[-.a-zA-Z0-9_]*;?\\)\\>"
				   "\\<\\(Td_[-.a-zA-Z0-9_]*;?\\)\\>"
				   "\\<\\(Hopla_[-.a-zA-Z0-9_]*;?\\)\\>"
))))

;; Divers
(fset 'yes-or-no-p 'y-or-n-p)
