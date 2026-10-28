# -*- coding: utf-8 -*-
"""
Author: Volkan Dindar
        volkan.dindar@owasp.org
        https://github.com/volkandindar/agartha
"""
try:
    import sys, re
    from burp import IBurpExtender, ITab
    from java.awt import BorderLayout, Color, Font, Dimension, Toolkit
    from javax.swing import (JCheckBox, JTextPane, GroupLayout, JScrollPane,
                             JComboBox, JButton, JTextField, JSplitPane, JPanel,
                             JLabel, JRadioButton, ButtonGroup, BoxLayout, SwingConstants)
    from javax.swing.border import EmptyBorder
    from java.awt.datatransfer import StringSelection
    from java.awt.event import MouseWheelListener, FocusListener
    from javax.swing.text import StyleConstants, StyleContext
except:
    print "==== ERROR ====" + "\n\nFailed to load dependencies.\n" + str(sys.exc_info()[1]) + "\n\n==== ERROR ====\n\n"
    sys.exit(1)

VERSION = "3.1010"


class BurpExtender(IBurpExtender, ITab):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._callbacks.setExtensionName("Agartha - Bambdas Generator")
        self._tabBambdasUI()
        callbacks.addSuiteTab(self)
        callbacks.issueAlert("Agartha Bambdas Generator loaded.")
        print "Agartha(v" + VERSION + ") - Bambdas Generator\n\nFor more information, please visit:\n\t\thttps://github.com/volkandindar/agartha\n\nAuthor:\n\t\tVolkan Dindar\n\t\tvolkan.dindar@owasp.org"
        return

    def getTabCaption(self):
        return "Agartha"

    def getUiComponent(self):
        return self._tabBambdasPanel

    def _cbBambdasValuableFunc(self, ev=None):
        if self._cbBambdasValuable.isSelected():
            self._txtBambdasValuable.setEnabled(True)
        else:
            self._txtBambdasValuable.setEnabled(False)

    def _cbBambdasFilesDownFunc(self, ev=None):
        if self._cbBambdasFilesDownloadable.isSelected():
            self._txtBambdasFilesDownloadable.setEnabled(True)
        else:
            self._txtBambdasFilesDownloadable.setEnabled(False)

    def _cbBambdasSQLiFunc(self, ev=None):
        if self._cbBambdasSQLi.isSelected():
            self._txtBambdasSQLiKeywords.setEnabled(True)
        else:
            self._txtBambdasSQLiKeywords.setEnabled(False)

    def _cbBambdasXSSFunc(self, ev=None):
        if self._cbBambdasXSS.isSelected():
            self._txtBambdasXSSKeywords.setEnabled(True)
        else:
            self._txtBambdasXSSKeywords.setEnabled(False)

    def _cbBambdasLFIFunc(self, ev=None):
        if self._cbBambdasLFI.isSelected():
            self._txtBambdasLFIKeywords.setEnabled(True)
        else:
            self._txtBambdasLFIKeywords.setEnabled(False)

    def _cbBambdasSSRFFunc(self, ev=None):
        if self._cbBambdasSSRF.isSelected():
            self._txtBambdasSSRFKeywords.setEnabled(True)
        else:
            self._txtBambdasSSRFKeywords.setEnabled(False)

    def _cbBambdasORedFunc(self, ev=None):
        if self._cbBambdasORed.isSelected():
            self._txtBambdasORedKeywords.setEnabled(True)
        else:
            self._txtBambdasORedKeywords.setEnabled(False)
    
    def _cbBambdasRCEFunc(self, ev=None):
        if self._cbBambdasRCE.isSelected():
            self._txtBambdasRCEKeywords.setEnabled(True)
        else:
            self._txtBambdasRCEKeywords.setEnabled(False)

    def _cbBambdasSearchinURLFunc(self, ev=None):
        if self._cbBambdasSearchinURL.isSelected():
            self._cbBambdasSQLi.setEnabled(True)
            if self._cbBambdasSQLi.isSelected():
                self._txtBambdasSQLiKeywords.setEnabled(True)
            self._cbBambdasXSS.setEnabled(True)
            if self._cbBambdasXSS.isSelected():
                self._txtBambdasXSSKeywords.setEnabled(True)
            self._cbBambdasLFI.setEnabled(True)
            if self._cbBambdasLFI.isSelected():
                self._txtBambdasLFIKeywords.setEnabled(True)
            self._cbBambdasSSRF.setEnabled(True)
            if self._cbBambdasSSRF.isSelected():
                self._txtBambdasSSRFKeywords.setEnabled(True)
            self._cbBambdasORed.setEnabled(True)
            if self._cbBambdasORed.isSelected():
                self._txtBambdasORedKeywords.setEnabled(True)
            self._cbBambdasRCE.setEnabled(True)
            if self._cbBambdasRCE.isSelected():
                self._txtBambdasRCEKeywords.setEnabled(True)
            self._cbBambdasValuable.setEnabled(True)
            if self._cbBambdasValuable.isSelected():
                self._txtBambdasValuable.setEnabled(True)
        else:
            if not self._cbBambdasSearchinReq.isSelected():
                self._cbBambdasSQLi.setEnabled(False)
                self._txtBambdasSQLiKeywords.setEnabled(False)
                self._cbBambdasXSS.setEnabled(False)
                self._txtBambdasXSSKeywords.setEnabled(False)
                self._cbBambdasLFI.setEnabled(False)
                self._txtBambdasLFIKeywords.setEnabled(False)
                self._cbBambdasSSRF.setEnabled(False)
                self._txtBambdasSSRFKeywords.setEnabled(False)
                self._cbBambdasORed.setEnabled(False)
                self._txtBambdasORedKeywords.setEnabled(False)
                self._cbBambdasRCE.setEnabled(False)
                self._txtBambdasRCEKeywords.setEnabled(False)
                if not self._cbBambdasSearchinRes.isSelected() and not self._cbBambdasSearchinReq.isSelected():
                    self._cbBambdasValuable.setEnabled(False)
                    self._txtBambdasValuable.setEnabled(False)

    def _cbBambdasSearchinReqFunc(self, ev=None):
        if self._cbBambdasSearchinReq.isSelected():
            self._cbBambdasSQLi.setEnabled(True)
            if self._cbBambdasSQLi.isSelected():
                self._txtBambdasSQLiKeywords.setEnabled(True)
            self._cbBambdasXSS.setEnabled(True)
            if self._cbBambdasXSS.isSelected():
                self._txtBambdasXSSKeywords.setEnabled(True)
            self._cbBambdasLFI.setEnabled(True)
            if self._cbBambdasLFI.isSelected():
                self._txtBambdasLFIKeywords.setEnabled(True)
            self._cbBambdasSSRF.setEnabled(True)
            if self._cbBambdasSSRF.isSelected():
                self._txtBambdasSSRFKeywords.setEnabled(True)
            self._cbBambdasORed.setEnabled(True)
            if self._cbBambdasORed.isSelected():
                self._txtBambdasORedKeywords.setEnabled(True)
            self._cbBambdasRCE.setEnabled(True)
            if self._cbBambdasRCE.isSelected():
                self._txtBambdasRCEKeywords.setEnabled(True)
            self._cbBambdasValuable.setEnabled(True)
            if self._cbBambdasValuable.isSelected():
                self._txtBambdasValuable.setEnabled(True)
        else:
            if not self._cbBambdasSearchinURL.isSelected():
                self._cbBambdasSQLi.setEnabled(False)
                self._txtBambdasSQLiKeywords.setEnabled(False)
                self._cbBambdasXSS.setEnabled(False)
                self._txtBambdasXSSKeywords.setEnabled(False)
                self._cbBambdasLFI.setEnabled(False)
                self._txtBambdasLFIKeywords.setEnabled(False)
                self._cbBambdasSSRF.setEnabled(False)
                self._txtBambdasSSRFKeywords.setEnabled(False)
                self._cbBambdasORed.setEnabled(False)
                self._txtBambdasORedKeywords.setEnabled(False)
                self._cbBambdasRCE.setEnabled(False)
                self._txtBambdasRCEKeywords.setEnabled(False)
                if not self._cbBambdasSearchinRes.isSelected() and not self._cbBambdasSearchinURL.isSelected():
                    self._cbBambdasValuable.setEnabled(False)
                    self._txtBambdasValuable.setEnabled(False)

    def _cbBambdasSearchinResFunc(self, ev=None):
        if self._cbBambdasSearchinRes.isSelected():
            self._cbBambdasSearchHTMLComments.setEnabled(True)
            self._cbBambdasFilesDownloadable.setEnabled(True)
            if self._cbBambdasFilesDownloadable.isSelected():
                self._txtBambdasFilesDownloadable.setEnabled(True)
            self._cbBambdasValuable.setEnabled(True)
            if self._cbBambdasValuable.isSelected():
                self._txtBambdasValuable.setEnabled(True)
            self._cbBambdasVulnJS.setEnabled(True)
            if self._cbBambdasVulnJS.isSelected():
                self._txtBambdasVulnJSKeywords.setEnabled(True)
        else:
            self._cbBambdasSearchHTMLComments.setEnabled(False)
            self._cbBambdasFilesDownloadable.setEnabled(False)
            self._txtBambdasFilesDownloadable.setEnabled(False)
            self._cbBambdasVulnJS.setEnabled(False)
            self._txtBambdasVulnJSKeywords.setEnabled(False)
            if not self._cbBambdasSearchinReq.isSelected() and not self._cbBambdasSearchinURL.isSelected():
                self._cbBambdasValuable.setEnabled(False)
                self._txtBambdasValuable.setEnabled(False)

    def _cbBambdasScopeFunc(self, ev=None):
        """Enable/disable the scope-mode radio buttons and the in-scope color picker."""
        if self._cbBambdasScope.isSelected():
            self._rbBambdasScopeHideShow.setEnabled(True)
            self._rbBambdasScopeHighlight.setEnabled(True)
            # Color picker is only relevant in Highlight mode
            self._cbBambdasColorInScope.setEnabled(self._rbBambdasScopeHighlight.isSelected())
        else:
            self._rbBambdasScopeHideShow.setEnabled(False)
            self._rbBambdasScopeHighlight.setEnabled(False)
            self._cbBambdasColorInScope.setEnabled(False)

    def _rbBambdasScopeFunc(self, ev=None):
        """Enable/disable the in-scope color picker based on the selected radio button."""
        self._cbBambdasColorInScope.setEnabled(
            self._cbBambdasScope.isSelected() and self._rbBambdasScopeHighlight.isSelected()
        )

    def _cbBambdasHTTPMethodsFunc(self, ev=None):
        if self._cbBambdasHTTPMethods.isSelected():
            self._txtBambdasHTTPMethods.setEnabled(True)
        else:
            self._txtBambdasHTTPMethods.setEnabled(False)
    
    def _cbBambdasVulnJSFunc(self, ev=None):
        if self._cbBambdasVulnJS.isSelected():
            self._txtBambdasVulnJSKeywords.setEnabled(True)
        else:
            self._txtBambdasVulnJSKeywords.setEnabled(False)

    def _cbBambdasExtIgnoreFunc(self, ev=None):
        if self._cbBambdasExtIgnore.isSelected():
            self._txtBambdasExtIgnoreKeywords.setEnabled(True)
        else:
            self._txtBambdasExtIgnoreKeywords.setEnabled(False)

    def funcBambdasRun(self, ev=None):

        if self._cbBambdasDisplayDays.getSelectedIndex() < self._cbBambdasProcessDays.getSelectedIndex():
            self._lblBambdasNotification2.text = "The display period must not be shorter than the processing period."
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        
        for line in self._tbBambdasScopeURLs.getText().splitlines():
            if self._tbBambdasScopeURLs.text != self._txBambdasScopeURLs and self._tbBambdasScopeURLs.text.strip() and line.strip():
                if line.strip().startswith("/*") or line.strip() == "/":
                    self._tbBambdasScopeURLs.setText("/")
                if " " in line.strip() and not line.strip().startswith("#"):
                    self._lblBambdasNotification2.text = "One or more of the test scope URLs contain spaces."
                    self._lblBambdasNotification2.setForeground(Color.red)
                    return
                if not line.strip().startswith("/") and not line.strip().startswith("#"):
                    self._lblBambdasNotification2.text = "Make sure all URLs in Testing Scope begin with a '/'"
                    self._lblBambdasNotification2.setForeground(Color.red)
                    return
        
        for line in self._tbBambdasScopeDoneURLs.getText().splitlines():
            if self._tbBambdasScopeDoneURLs.text != self._txBambdasScopeDoneURLs and self._tbBambdasScopeDoneURLs.text and line.strip():
                if line.strip().startswith("/*") or line.strip() == "/":
                    self._lblBambdasNotification2.text = "You can not set root directory '/' in the tested URLs."
                    self._lblBambdasNotification2.setForeground(Color.red)
                    return
                if " " in line.strip() and not line.strip().startswith("#"):
                    self._lblBambdasNotification2.text = "One or more of the tested URLs contain spaces."
                    self._lblBambdasNotification2.setForeground(Color.red)
                    return
                if not line.strip().startswith("/") and not line.strip().startswith("#"):
                    self._lblBambdasNotification2.text = "Make sure all URLs in Tested section begin with a '/'"
                    self._lblBambdasNotification2.setForeground(Color.red)
                    return

        for line in self._tbBambdasBlackListedURLs.getText().splitlines():
            if self._tbBambdasBlackListedURLs.text != self._txBambdasBlackListedURLs and self._tbBambdasBlackListedURLs.text.strip() and line.strip():
                if line.strip().startswith("/*") or line.strip() == "/":
                    self._tbBambdasBlackListedURLs.setText("/")
                    if self._tbBambdasScopeURLs.text == self._txBambdasScopeURLs or not self._tbBambdasScopeURLs.text.strip():
                        self._lblBambdasNotification2.text = "Root directory '/' can't be blacklisted, unless you provide scope URLs."
                        self._lblBambdasNotification2.setForeground(Color.red)
                        return
                if " " in line.strip() and not line.strip().startswith("#"):
                    self._lblBambdasNotification2.text = "One or more of the Black-Listed URLs contain spaces."
                    self._lblBambdasNotification2.setForeground(Color.red)
                    return
                if not line.strip().startswith("/") and not line.strip().startswith("#"):
                    self._lblBambdasNotification2.text = "Make sure all URL in Black-Listed section begin with a '/'"
                    self._lblBambdasNotification2.setForeground(Color.red)
                    return

        if self._cbBambdasHTTPMethods.isSelected() and self._txtBambdasHTTPMethods.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The HTTP methods option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasValuable.isSelected() and self._txtBambdasValuable.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The Valuable keywords option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasFilesDownloadable.isSelected() and self._txtBambdasFilesDownloadable.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The Downloadable file extensions option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasSQLi.isSelected() and self._txtBambdasSQLiKeywords.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The SQLi-suspect identifiers option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasXSS.isSelected() and self._txtBambdasXSSKeywords.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The XSS-suspect identifiers option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasLFI.isSelected() and self._txtBambdasLFIKeywords.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The LFI-suspect identifiers option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasSSRF.isSelected() and self._txtBambdasSSRFKeywords.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The SSRF-suspect identifiers option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasORed.isSelected() and self._txtBambdasORedKeywords.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The Open Redirect-suspect identifiers option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasRCE.isSelected() and self._txtBambdasRCEKeywords.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The RCE-suspect identifiers option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasVulnJS.isSelected() and self._txtBambdasVulnJSKeywords.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The Vulnerable JS Functions option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return
        if self._cbBambdasExtIgnore.isSelected() and self._txtBambdasExtIgnoreKeywords.text.strip().replace(",","") == "" :
            self._lblBambdasNotification2.text = "The File extensions to ignore option is selected, but no input has been provided"
            self._lblBambdasNotification2.setForeground(Color.red)
            return

        # --- Snapshot placeholder state BEFORE any mutation of the text panes ---
        # We compare stripped versions so minor whitespace/newline differences
        # introduced by setText() round-trips can never fool the check.
        _scopeHasUserInput = (
            bool(self._tbBambdasScopeURLs.text.strip()) and
            self._tbBambdasScopeURLs.text.strip() != self._txBambdasScopeURLs.strip()
        )
        _scopeDoneHasUserInput = (
            bool(self._tbBambdasScopeDoneURLs.text.strip()) and
            self._tbBambdasScopeDoneURLs.text.strip() != self._txBambdasScopeDoneURLs.strip()
        )
        _blackListHasUserInput = (
            bool(self._tbBambdasBlackListedURLs.text.strip()) and
            self._tbBambdasBlackListedURLs.text.strip() != self._txBambdasBlackListedURLs.strip()
        )

        # remove white-spaces (only when the field has real content)
        if _scopeHasUserInput:
            self._tbBambdasScopeURLs.setText("\n".join(l.strip() for l in self._tbBambdasScopeURLs.getText().splitlines()))
        if _scopeDoneHasUserInput:
            self._tbBambdasScopeDoneURLs.setText("\n".join(l.strip() for l in self._tbBambdasScopeDoneURLs.getText().splitlines()))
        if _blackListHasUserInput:
            self._tbBambdasBlackListedURLs.setText("\n".join(l.strip() for l in self._tbBambdasBlackListedURLs.getText().splitlines()))
        # remove white-spaces
        # Filter out scope lines that have already been tested (only when both fields have real content)
        if _scopeHasUserInput:
            urls_lines = self._tbBambdasScopeURLs.getText().split("\n")
            done_urls_lines = set(self._tbBambdasScopeDoneURLs.getText().split("\n"))
            new_urls_lines = [line if line.startswith("#") or re.sub(r"\{[^}]+\}|\*", ".*", line) not in {re.sub(r"\{[^}]+\}|\*", ".*", l) for l in done_urls_lines} else "" for line in urls_lines]
            self._tbBambdasScopeURLs.setText("\n".join(new_urls_lines))
        # Filter out scope lines that have already been tested

        bambdas = "/**\n"
        bambdas += " * Bambdas Script - generated by Agartha\n"
        bambdas += " **/\n\n"

        bambdas += "// If true: clear highlights and notes, then stop. If false: execute the script.\n"
        bambdas += "boolean resetScreen = false;\n"
        bambdas += "// Toggle above when you want to wipe colors/notes without running checks.\n\n"

        bambdas += "// Testing scope URLs. \n"
        if _scopeHasUserInput and sum(1 for line in self._tbBambdasScopeURLs.text.splitlines() if line.strip() == '/') == 1:
            bambdas += "String[] targetPaths = {\"/.*\"};\n"
        elif _scopeHasUserInput:
            targetPaths = "{"
            for line in list(dict.fromkeys(self._tbBambdasScopeURLs.text.splitlines())):
                if line.strip() and not line.strip().startswith("#"):
                    targetPaths += "\"" + (re.sub(r"\{[^}]+\}|\*", ".*", line.strip()) + "/?(?:\\\\?.*)?$") + "\", "
            if targetPaths != "{":
                targetPaths = targetPaths[:-2]
            targetPaths += "}"
            bambdas += "String[] targetPaths = " + targetPaths + ";\n"
        else:
            # No testing scope defined: empty array so the coloring loop never fires
            bambdas += "String[] targetPaths = {};\n"
        bambdas += "// Define the URLs you want to actively assess here.\n\n"

        if _blackListHasUserInput and self._tbBambdasBlackListedURLs.getText() != '/':
            bambdas += "// Black-Listed / Unwanted URLs\n"
            targetBlackListUrls = "{"
            for line in list(dict.fromkeys(self._tbBambdasBlackListedURLs.text.splitlines())):
                if line.strip() and not line.strip().startswith("#"):
                    targetBlackListUrls += "\"" + (re.sub(r"\{[^}]+\}|\*", ".*", line.strip()) + "/?(?:\\\\?.*)?$") + "\", "
            if targetBlackListUrls != "{":
                targetBlackListUrls = targetBlackListUrls[:-2]
            targetBlackListUrls += "}"
            bambdas += "String[] targetBlackListUrls = " + targetBlackListUrls + ";\n"
            bambdas += "// Add patterns here to ignore noise (health checks, static banners, monitor, etc.).\n"
            bambdas += "\n"

        bambdas += "// Already-tested URLs (mark as completed).\n"
        if _scopeDoneHasUserInput:
            targetPaths = "{"
            for line in list(dict.fromkeys(self._tbBambdasScopeDoneURLs.text.splitlines())):
                if line.strip() and not line.strip().startswith("#"):
                    targetPaths += "\"" + (re.sub(r"\{[^}]+\}|\*", ".*", line.strip()) + "/?(?:\\\\?.*)?$") + "\", "
            if targetPaths != "{":
                targetPaths = targetPaths[:-2]
            targetPaths += "}"
            bambdas += "String[] targetPathsDone = " + targetPaths + ";\n"
        else:
            bambdas += "String[] targetPathsDone = {\"/YouCanPutTestedURLsHere/?(?:\\\\?.*)?$\"};\n"
        bambdas += "// Move stable/assessed endpoints here to avoid re-triage.\n\n"

        bambdas += "// Reset mode: clear all highlights and notes, then exit.\n"
        bambdas += "if (resetScreen) {\n"
        bambdas += "    requestResponse.annotations().setHighlightColor(HighlightColor.NONE);\n"
        bambdas += "    requestResponse.annotations().setNotes(\"\");\n"
        bambdas += "    return true;\n"
        bambdas += "}\n"
        bambdas += "// Reset mode: clear all highlights and notes, then exit.\n\n"
        
        bambdas += "// Display window (days): ignore items older than the selected number of days\n"
        bambdas += "if (!requestResponse.time().isAfter(ZonedDateTime.now().minusDays(" + self._cbBambdasDisplayDays.getSelectedItem().split()[0] + ")))\n"
        bambdas += "    return false;\n\n"

        if self._cbBambdasScope.isSelected():
            if self._rbBambdasScopeHideShow.isSelected():
                bambdas += "// Display only items that are in scope and have a response.\n"
                bambdas += "if (!requestResponse.hasResponse() || !requestResponse.request().isInScope())\n"
            else:
                # Highlight mode: still show everything, but note scope status for later coloring
                bambdas += "// Display only items that have a response (scope items will be highlighted later).\n"
                bambdas += "if (!requestResponse.hasResponse())\n"
        else:
            bambdas += "// Display only items that have a response\n"
            bambdas += "if (!requestResponse.hasResponse())\n"
        bambdas += "    return false;\n\n"

        if self._cbBambdasHTTPMethods.isSelected():
            httpMethods = "{"
            for httpMtd in [httpMtd.strip() for httpMtd in self._txtBambdasHTTPMethods.text.strip().split(',')]:
                if httpMtd:
                    httpMethods += "\"" + httpMtd + "\", "
            if httpMethods != "{":
                httpMethods = httpMethods[:-2] 
            httpMethods += "}"
            bambdas += "// HTTP methods to ignore\n"
            bambdas += "String[] httpMethods = " + httpMethods + ";"
            bambdas +="""
for (String httpMethod : httpMethods)
    if (requestResponse.request().method().equalsIgnoreCase(httpMethod))
        return false;
// HTTP methods to ignore\n
"""

        bambdas += "// General vars\n"
        bambdas += "boolean suspiciousHit = false;\n"
        bambdas += "boolean matchedScope = false;\n"
        bambdas += "boolean matchedDone = false;\n"
        bambdas += "StringBuilder notesBuilder = new StringBuilder();\n"
        if self._cbBambdasSearchinRes.isSelected() and (self._cbBambdasSearchHTMLComments.isSelected() or self._cbBambdasFilesDownloadable.isSelected() or self._cbBambdasValuable.isSelected() or self._cbBambdasVulnJS.isSelected()):
            bambdas += "String responseBody = requestResponse.response().bodyToString();\n"
            if self._cbBambdasFilesDownloadable.isSelected():
                bambdas += """StringBuilder headersString = new StringBuilder();
boolean isDownloadHeaderPresent = false;
List<HttpHeader> responseHeaders = requestResponse.response().headers();
for (HttpHeader header : responseHeaders) {
    if (header.name().equalsIgnoreCase("Content-Disposition"))
        isDownloadHeaderPresent = true;
    headersString.append(header.name()).append(": ").append(header.value()).append("\\n");
}
String responseHeader = isDownloadHeaderPresent ? headersString.toString() : "";
"""
        if (self._cbBambdasSearchinReq.isSelected() or self._cbBambdasSearchinURL.isSelected()) and (self._cbBambdasSQLi.isSelected() or self._cbBambdasXSS.isSelected() or self._cbBambdasLFI.isSelected() or self._cbBambdasSSRF.isSelected() or self._cbBambdasORed.isSelected() or self._cbBambdasRCE.isSelected() or self._cbBambdasValuable.isSelected()):
            bambdas += "String requestBody  = requestResponse.request().bodyToString();\n"
        bambdas += "var path = requestResponse.request().path().toLowerCase();\n"
        bambdas += "var pathExt = requestResponse.request().pathWithoutQuery().toLowerCase();\n"
        bambdas += "// General vars\n\n"

        if self._tbBambdasBlackListedURLs.getText() != '/' and self._tbBambdasBlackListedURLs.getText().strip() and self._tbBambdasBlackListedURLs.getText() != self._txBambdasBlackListedURLs:
            bambdas += "// Apply blacklist to skip unwanted URLs\n"
            bambdas += "for (String targetPath : targetBlackListUrls)\n"
            bambdas += "    if (targetPath != null && !targetPath.trim().isEmpty() && Pattern.compile(targetPath, Pattern.CASE_INSENSITIVE).matcher(path).find())\n"
            bambdas += "        return false;\n"
            bambdas += "// Apply blacklist to skip unwanted URLs\n\n"

        if self._cbBambdasExtIgnore.isSelected():
            filterDenyList = ""
            for ext in [ext.strip() for ext in self._txtBambdasExtIgnoreKeywords.text.split(',')]:
                filterDenyList += "|" + ext;
            if filterDenyList[1:]:
                bambdas += "// Ignore static asset extensions to reduce noise.\n"
                bambdas += "if (Pattern.compile(\"\\\\.(" + filterDenyList[1:] + ")$\", Pattern.CASE_INSENSITIVE).matcher(pathExt).find())\n"
                bambdas += "    return false;\n"
                bambdas += "// Ignore static asset extensions to reduce noise.\n\n"

        bambdas += "// Processing window (days): only analyze items newer than this threshold\n"
        bambdas += "if (requestResponse.time().isAfter(ZonedDateTime.now().minusDays(" + self._cbBambdasProcessDays.getSelectedItem().split()[0] + "))){\n"

        if (self._cbBambdasSearchinReq.isSelected() or self._cbBambdasSearchinURL.isSelected()) and (self._cbBambdasSQLi.isSelected() or self._cbBambdasXSS.isSelected() or self._cbBambdasLFI.isSelected() or self._cbBambdasSSRF.isSelected() or self._cbBambdasORed.isSelected() or self._cbBambdasRCE.isSelected()):
            bambdas += "\t// Suspicious parameter registry per attack type\n"
            bambdas += "\n\tMap<String, List<String>> attacksKeyWords = new HashMap<>();\n"
            bambdas += "\tString[] paramsArray;\n"
            bambdas += "\tList<String> paramsArrayTrimmed = new ArrayList<>();\n\n"
        
            if self._cbBambdasSQLi.isSelected():
                bambdas += "\t// SQLi indicator parameter names\n"
                bambdas += "\tparamsArrayTrimmed = new ArrayList<>();\n"
                bambdas += "\tString textSQLi = \"" + self._txtBambdasSQLiKeywords.text.strip() + "\";\n"
                bambdas += "\tparamsArray = textSQLi.split(\",\\s*\");\n"
                bambdas += "\tfor (String paramArray : paramsArray)\n"
                bambdas += "\t\tif(!paramArray.trim().isEmpty())\n"
                bambdas += "\t\t\tparamsArrayTrimmed.add(paramArray.trim());\n"
                bambdas += "\tattacksKeyWords.put(\"SQLi\", new ArrayList<>(paramsArrayTrimmed));\n\n"

            if self._cbBambdasXSS.isSelected():
                bambdas += "\t// XSS indicator parameter names\n"
                bambdas += "\tparamsArrayTrimmed = new ArrayList<>();\n"
                bambdas += "\tString textXSS = \"" + self._txtBambdasXSSKeywords.text.strip() + "\";\n"
                bambdas += "\tparamsArray = textXSS.split(\",\\s*\");\n"
                bambdas += "\tfor (String paramArray : paramsArray)\n"
                bambdas += "\t\tif(!paramArray.trim().isEmpty())\n"
                bambdas += "\t\t\tparamsArrayTrimmed.add(paramArray.trim());\n"
                bambdas += "\tattacksKeyWords.put(\"XSS\", new ArrayList<>(paramsArrayTrimmed));\n\n"

            if self._cbBambdasLFI.isSelected():
                bambdas += "\t// LFI indicator parameter names (file/path handling)\n"
                bambdas += "\tparamsArrayTrimmed = new ArrayList<>();\n"
                bambdas += "\tString textLFI = \"" + self._txtBambdasLFIKeywords.text.strip() + "\";\n"
                bambdas += "\tparamsArray = textLFI.split(\",\\s*\");\n"
                bambdas += "\tfor (String paramArray : paramsArray)\n"
                bambdas += "\t\tif(!paramArray.trim().isEmpty())\n"
                bambdas += "\t\t\tparamsArrayTrimmed.add(paramArray.trim());\n"
                bambdas += "\tattacksKeyWords.put(\"LFI\", new ArrayList<>(paramsArrayTrimmed));\n\n"

            if self._cbBambdasSSRF.isSelected():
                bambdas += "\t// SSRF indicator parameter names (URLs/redirects)\n"
                bambdas += "\tparamsArrayTrimmed = new ArrayList<>();\n"
                bambdas += "\tString textSSRF = \"" + self._txtBambdasSSRFKeywords.text.strip() + "\";\n"
                bambdas += "\tparamsArray = textSSRF.split(\",\\s*\");\n"
                bambdas += "\tfor (String paramArray : paramsArray)\n"
                bambdas += "\t\tif(!paramArray.trim().isEmpty())\n"
                bambdas += "\t\t\tparamsArrayTrimmed.add(paramArray.trim());\n"
                bambdas += "\tattacksKeyWords.put(\"SSRF\", new ArrayList<>(paramsArrayTrimmed));\n\n"

            if self._cbBambdasORed.isSelected():
                bambdas += "\t// Open Redirect indicator parameter names\n"
                bambdas += "\tparamsArrayTrimmed = new ArrayList<>();\n"
                bambdas += "\tString textOR = \"" + self._txtBambdasORedKeywords.text.strip() + "\";\n"
                bambdas += "\tparamsArray = textOR.split(\",\\s*\");\n"
                bambdas += "\tfor (String paramArray : paramsArray)\n"
                bambdas += "\t\tif(!paramArray.trim().isEmpty())\n"
                bambdas += "\t\t\tparamsArrayTrimmed.add(paramArray.trim());\n"
                bambdas += "\tattacksKeyWords.put(\"OpenRedirect\", new ArrayList<>(paramsArrayTrimmed));\n\n"

            if self._cbBambdasRCE.isSelected():
                bambdas += "\t// RCE - command-execution indicator parameter names\n"
                bambdas += "\tparamsArrayTrimmed = new ArrayList<>();\n"
                bambdas += "\tString textRCE = \"" + self._txtBambdasRCEKeywords.text.strip() + "\";\n"
                bambdas += "\tparamsArray = textRCE.split(\",\\s*\");\n"
                bambdas += "\tfor (String paramArray : paramsArray)\n"
                bambdas += "\t\tif(!paramArray.trim().isEmpty())\n"
                bambdas += "\t\t\tparamsArrayTrimmed.add(paramArray.trim());\n"
                bambdas += "\tattacksKeyWords.put(\"RCE\", new ArrayList<>(paramsArrayTrimmed));\n\n"

            bambdas += "\t// End suspicious parameter registry\n\n"
        
        if self._cbBambdasValuable.isSelected() and (self._cbBambdasSearchinReq.isSelected() or self._cbBambdasSearchinRes.isSelected() or self._cbBambdasSearchinURL.isSelected()):
            bambdas += "\t// High-value keywords to search\n"
            highValueWords = "{"
            for valueWords in [valueWords.strip() for valueWords in self._txtBambdasValuable.text.strip().split(',')]:
                if valueWords:
                    highValueWords += "\"" + valueWords + "\", "
            if highValueWords != "{":
                highValueWords = highValueWords[:-2] 
            highValueWords += "}"
            bambdas += "\tString[] highValueWords = " + highValueWords + ";\n"
            bambdas += "\t// High-value keywords to search\n\n"

        if self._cbBambdasSearchinRes.isSelected():
            if self._cbBambdasVulnJS.isSelected():
                vulnJSFunc = "{"
                for vulnJS in [vulnJS.strip() for vulnJS in self._txtBambdasVulnJSKeywords.text.strip().replace(".","\\\\.").replace("(","\\\\(").split(',')]:
                    if vulnJS:
                        vulnJSFunc += "\"" + vulnJS + "\", "
                if vulnJSFunc != "{":
                    vulnJSFunc = vulnJSFunc[:-2] 
                vulnJSFunc += "}"
                bambdas += "\t// Potentially risky JavaScript functions to look for in responses\n"
                bambdas += "\tString[] suspiciousFunctions = " + vulnJSFunc + ";\n"
                bambdas += "\t// Potentially risky JavaScript functions to look for in responses\n\n"

            if self._cbBambdasFilesDownloadable.isSelected():
                fileExtensions = "{"
                for ext in [ext.strip() for ext in self._txtBambdasFilesDownloadable.text.strip().split(',')]:
                    if ext:
                        fileExtensions += "\"" + ext + "\", "
                if fileExtensions != "{":
                    fileExtensions = fileExtensions[:-2] 
                fileExtensions += "}"
                bambdas += "\t// Potentially downloadable file extensions\n"
                bambdas += "\tString[] fileExtensions = " + fileExtensions + ";\n"
                bambdas += "\t// Potentially downloadable file extensions\n\n"
                
        if self._cbBambdasValuable.isSelected() and (self._cbBambdasSearchinReq.isSelected() or self._cbBambdasSearchinRes.isSelected() or self._cbBambdasSearchinURL.isSelected()):
            bambdas += """
    List<Pattern> patterns = new ArrayList<>();
    for (String highValueWord : highValueWords)
        patterns.add(Pattern.compile(highValueWord, Pattern.CASE_INSENSITIVE));
"""
            if self._cbBambdasSearchinRes.isSelected():
                bambdas += """
    // High-value keyword - from response body
    for (Pattern pattern : patterns)
        if (pattern.matcher(responseBody).find()){
            suspiciousHit = true;
            if (notesBuilder.length() > 0)
                notesBuilder.append(", ");
            notesBuilder.append(pattern + " (ValuableWord-Res)");
        }
"""
            if self._cbBambdasSearchinReq.isSelected():
                bambdas += """
    // High-value keyword - from request body
    for (Pattern pattern : patterns)
        if (pattern.matcher(requestBody).find()){
            suspiciousHit = true;
            if (notesBuilder.length() > 0)
                notesBuilder.append(", ");
            notesBuilder.append(pattern + " (ValuableWord-Req)");
        }
"""
            if self._cbBambdasSearchinURL.isSelected():
                bambdas += """
    // High-value keyword - from URL
    for (Pattern pattern : patterns)
        if (pattern.matcher(path).find()){
            suspiciousHit = true;
            if (notesBuilder.length() > 0)
                notesBuilder.append(", ");
            notesBuilder.append(pattern + " (ValuableWord-URL)");
        }
"""
        if self._cbBambdasSearchinRes.isSelected():
            if not self._cbBambdasValuable.isSelected():
                bambdas += "\tList<Pattern> patterns = new ArrayList<>();"

            if self._cbBambdasFilesDownloadable.isSelected():
                bambdas += """
    // Potential downloads referenced in the response (by extension match)
    patterns = new ArrayList<>();
    for (String ext : fileExtensions)
        patterns.add(Pattern.compile("[\\\\s/>]?[^\\"'\\\\s<>]+\\\\." + ext + "(?=[\\\\s\\"])", Pattern.CASE_INSENSITIVE));
    
    ArrayList<String> matchingFiles = new ArrayList<>();
    // Scan response for suspected downloadable files
    List<String> sourcesToCheck = Arrays.asList(responseBody, responseHeader);
    for (String source : sourcesToCheck) {
        if (!source.isEmpty()) { 
            for (Pattern pattern : patterns) {
                Matcher matcher = pattern.matcher(source);
                while (matcher.find()) {
                    suspiciousHit = true;
                    String matchingFile = matcher.group();
                    matchingFiles.add(matchingFile);
                    if (notesBuilder.length() > 0)
                        notesBuilder.append(", ");
                    notesBuilder.append(matchingFile.strip().replace(">", "").replace("\\"", "")).append(" (Potential-FileDownload)");
                }
            }
        }
    }
"""
            if self._cbBambdasSearchHTMLComments.isSelected():
                bambdas += """
    // HTML comments in response
    patterns = new ArrayList<>();
    patterns.add(Pattern.compile(\"<!--.*?-->\", Pattern.DOTALL));
    ArrayList<String> matchingComments = new ArrayList<>();
    for (Pattern pattern : patterns) {
        Matcher matcher = pattern.matcher(responseBody);
        while (matcher.find()) {
            suspiciousHit = true;
            String matchingComment = matcher.group();
            matchingComments.add(matchingComment);
            if (notesBuilder.length() > 0)
                notesBuilder.append(\", \");
            notesBuilder.append(matchingComment).append(\" (HTML-Comment)\");
        }
    }
"""

            if self._cbBambdasVulnJS.isSelected():
                bambdas += """
    // Potentially risky JavaScript functions observed in the response
    patterns = new ArrayList<>();
    for (String suspiciousFunction : suspiciousFunctions)
        patterns.add(Pattern.compile(suspiciousFunction, Pattern.CASE_INSENSITIVE));
    
    for (Pattern pattern : patterns) {
        if (pattern.matcher(responseBody).find()){
                suspiciousHit = true;
                if (notesBuilder.length() > 0)
                    notesBuilder.append(", ");
                notesBuilder.append(pattern.toString().replace("\\\\", "")  + " - (VulnJSFunc)");
            }
        }
"""
        if (self._cbBambdasSearchinURL.isSelected() or self._cbBambdasSearchinReq.isSelected()) and (self._cbBambdasSQLi.isSelected() or self._cbBambdasXSS.isSelected() or self._cbBambdasLFI.isSelected() or self._cbBambdasSSRF.isSelected() or self._cbBambdasORed.isSelected() or self._cbBambdasRCE.isSelected()):
            if not self._cbBambdasValuable.isSelected() and not self._cbBambdasSearchinRes.isSelected():
                bambdas += "\tList<Pattern> patterns = new ArrayList<>();"

            bambdas += """
    // Parameter-based indicators across URL/query and request body
    for (Map.Entry<String, List<String>> entry : attacksKeyWords.entrySet()) {
        String attackType = entry.getKey();
        List<String> attackParams = entry.getValue();
        boolean htmlContent = false;
        patterns = new ArrayList<>();
        if (requestBody.startsWith("<"))
            // xml body
            for (String attackParam : attackParams)
                patterns.add(Pattern.compile("<" + attackParams + ">", Pattern.CASE_INSENSITIVE));
        else if (requestBody.startsWith("[{") || requestBody.startsWith("{"))
            // json body
            for (String attackParam : attackParams)
                patterns.add(Pattern.compile("\\\"" + attackParam + "\\\"", Pattern.CASE_INSENSITIVE));
        else {
            // regular html
            htmlContent = true;
            for (String attackParam : attackParams)
                patterns.add(Pattern.compile(attackParam, Pattern.CASE_INSENSITIVE));
            }

        if (htmlContent)
            // regular html
            for (String attackParam : attackParams){
"""
            if self._cbBambdasSearchinURL.isSelected():
                bambdas += """
                if (requestResponse.request().hasParameter(attackParam, HttpParameterType.URL)){
                    suspiciousHit = true;
                    if (notesBuilder.length() > 0)
                        notesBuilder.append(", ");
                    notesBuilder.append(attackParam + " (" + attackType + "-URL param)");
                }
"""
            if self._cbBambdasSearchinReq.isSelected():
                bambdas += """
                if (requestResponse.request().hasParameter(attackParam, HttpParameterType.BODY)){
                    suspiciousHit = true;
                    if (notesBuilder.length() > 0)
                        notesBuilder.append(", ");
                    notesBuilder.append(attackParam + " (" + attackType + "-Req param)");
                }
"""
            bambdas += "\t\t\t}\n"
                
            if self._cbBambdasSearchinReq.isSelected():
                bambdas += """
        else
            // xml or json
            for (Pattern pattern : patterns)
                if (pattern.matcher(requestBody).find()){
                    suspiciousHit = true;
                    if (notesBuilder.length() > 0)
                        notesBuilder.append(", ");
                    notesBuilder.append(pattern.toString().replace("\\\\", "") + " (" + attackType + "-Req param)");
                }
"""
            bambdas +="\n\t}\n\t// End parameter-based indicators\n"

        if (self._cbBambdasSearchinURL.isSelected() or self._cbBambdasSearchinReq.isSelected() or self._cbBambdasSearchinRes.isSelected()) and (self._cbBambdasSQLi.isSelected() or self._cbBambdasXSS.isSelected() or self._cbBambdasLFI.isSelected() or self._cbBambdasSSRF.isSelected() or self._cbBambdasORed.isSelected() or self._cbBambdasRCE.isSelected() or self._cbBambdasSearchHTMLComments.isSelected() or self._cbBambdasFilesDownloadable.isSelected() or self._cbBambdasVulnJS.isSelected() or self._cbBambdasValuable.isSelected()):
            bambdas +="\n\t// Apply highlight and add a consolidated \"Suspicious:\" note if any hit was found\n"
            bambdas += "\tif (suspiciousHit) {\n"
            bambdas += "\t\trequestResponse.annotations().setHighlightColor(HighlightColor."+ self._cbBambdasColorKeyWords.getSelectedItem() + ");\n"
            bambdas += """
        if (notesBuilder.length() > 0)
            requestResponse.annotations().setNotes("Suspicious: " + notesBuilder.toString());
        }
"""
        bambdas += """
    // clear notes and colors if no match
    if (!suspiciousHit){
            requestResponse.annotations().setHighlightColor(HighlightColor.NONE);
            requestResponse.annotations().setNotes("");
    }

"""
        # Highlight mode: color items that are within the Burp Suite project scope
        if self._cbBambdasScope.isSelected() and self._rbBambdasScopeHighlight.isSelected():
            inScopeColor = self._cbBambdasColorInScope.getSelectedItem()
            bambdas += "    // Highlight items that are within the Burp Suite project scope\n"
            bambdas += "    if (requestResponse.request().isInScope())"
            if inScopeColor != "NONE":
                bambdas += " {\n"
                bambdas += "        requestResponse.annotations().setHighlightColor(HighlightColor." + inScopeColor + ");\n"
                bambdas += "    }\n\n"
            else:
                bambdas += " { /* color is NONE – no highlight applied */ }\n\n"

        bambdas += """    // Highlight items that match testing scope
    for (String targetPath : targetPaths)
        if (Pattern.compile(targetPath, Pattern.CASE_INSENSITIVE).matcher(path).find() && targetPath != null && !targetPath.trim().isEmpty()"""
        # In Highlight mode the loop must additionally check Burp project scope,
        # otherwise every host that matches the path pattern would get coloured.
        if self._cbBambdasScope.isSelected() and self._rbBambdasScopeHighlight.isSelected():
            bambdas += " && requestResponse.request().isInScope()"
        if self._cbBambdasColorScope.getSelectedIndex() == 0:
            bambdas += " && (requestResponse.annotations().highlightColor() == HighlightColor.NONE)"
        bambdas += "){\n"
        bambdas += "\t\t\trequestResponse.annotations().setHighlightColor(HighlightColor."+ self._cbBambdasColorScope.getSelectedItem() + ");\n\t\t\tmatchedScope = true;\n\t\t\tbreak;\n\t\t\t}\n"

        bambdas += """
    // Highlight items already marked as tested
    for (String targetPath : targetPathsDone)
        if (Pattern.compile(targetPath, Pattern.CASE_INSENSITIVE).matcher(path).find() && targetPath != null && !targetPath.trim().isEmpty()"""
        if self._cbBambdasColorScopeSecondary.getSelectedIndex() == 0:
            bambdas += " && (requestResponse.annotations().highlightColor() == HighlightColor.NONE)"
        bambdas += "){\n"
        bambdas += "\t\t\trequestResponse.annotations().setHighlightColor(HighlightColor."+ self._cbBambdasColorScopeSecondary.getSelectedItem() + ");\n\t\t\tmatchedDone = true;\n\t\t\tbreak;\n\t\t}\n}\n// End processing window"

        bambdas += """
// clear anything outside of processing window
else {
    requestResponse.annotations().setHighlightColor(HighlightColor.NONE);
    requestResponse.annotations().setNotes("");
}
"""
        if self._tbBambdasBlackListedURLs.getText() == '/':
            bambdas += """
// Root blacklist (/) selected: ignore everything unless a matching criterion is found (scope, tested, or suspicious flags)."
if (!suspiciousHit && !matchedScope && !matchedDone)
    return false;
"""
        bambdas += "\nreturn true;"

        allUrls = False
        allUrlsBlacklisted = False
        if not _scopeHasUserInput or sum(1 for line in self._tbBambdasScopeURLs.text.splitlines() if line.strip() == '/') == 1:
            allUrls = True
        if sum(1 for line in self._tbBambdasBlackListedURLs.text.splitlines() if line.strip() == '/') == 1:
            allUrlsBlacklisted = True

        self._lblBambdasNotification2.setForeground(Color.black)
        if allUrls:
            self._lblBambdasNotification2.text = "The script has been generated and copied to the clipboard. It includes all endpoints, with '"  + str(sum(1 for line in self._tbBambdasScopeDoneURLs.text.splitlines() if line.strip().startswith('/'))) + "' tested, and '" + str(sum(1 for line in self._tbBambdasBlackListedURLs.text.splitlines() if line.strip().startswith('/'))) + "' blacklisted."
        else:
            if allUrlsBlacklisted:
                self._lblBambdasNotification2.text = "The script has been generated and copied to the clipboard. It includes '" + str(sum(1 for line in self._tbBambdasScopeURLs.text.splitlines() if line.strip().startswith('/'))) + "' scoped, and '" + str(sum(1 for line in self._tbBambdasScopeDoneURLs.text.splitlines() if line.strip().startswith('/'))) + "' tested endpoints - the rest are hidden."
            else:
                self._lblBambdasNotification2.text = "The script has been generated and copied to the clipboard. It includes '" + str(sum(1 for line in self._tbBambdasScopeURLs.text.splitlines() if line.strip().startswith('/'))) + "' scoped, '" + str(sum(1 for line in self._tbBambdasScopeDoneURLs.text.splitlines() if line.strip().startswith('/'))) + "' tested, and '" + str(sum(1 for line in self._tbBambdasBlackListedURLs.text.splitlines() if line.strip().startswith('/'))) + "' blacklisted endpoints."

        self.updateBambdasScriptText(bambdas)

        clipboard = Toolkit.getDefaultToolkit().getSystemClipboard()
        clipboard.setContents(StringSelection(bambdas), None)

        return

    def updateBambdasScriptText(self, javaCode):

        doc = self._tbBambdasScript.getStyledDocument()
        processWhat = ""
        if javaCode.startswith("/*"):
            doc = self._tbBambdasScript.getStyledDocument()
            processWhat = "Bambdas"
        elif javaCode.startswith("metadata"):
            if javaCode.count("\n") > 3000:
                # do not color if more then 3000 lines
                self._tabDictResultDisplay.setText(javaCode)
                return
            doc = self._tabDictResultDisplay.getStyledDocument()
            processWhat = "Dict"
        else:
            # no match no coloring
            self._tabDictResultDisplay.setText(javaCode)
            return

        doc.remove(0, doc.getLength())

        # Define styles
        style_default = StyleContext.getDefaultStyleContext().getStyle(StyleContext.DEFAULT_STYLE)

        style_comment = doc.addStyle("comment", style_default)
        StyleConstants.setForeground(style_comment, Color(0, 150, 0))

        style_string = doc.addStyle("string", style_default)
        StyleConstants.setForeground(style_string, Color(0, 102, 204))

        style_annotation = doc.addStyle("annotation", style_default)
        StyleConstants.setForeground(style_annotation, Color(160, 100, 100))

        style_keyword = doc.addStyle("keyword", style_default)
        StyleConstants.setForeground(style_keyword, Color(153, 0, 153))

        style_normal = doc.addStyle("normal", style_default)
        StyleConstants.setForeground(style_normal, Color.BLACK)

        # Define regex patterns in priority order
        patterns = [
            (r'/\*[\s\S]*?\*/', style_comment),  # Multi-line comments
            (r'//.*', style_comment),            # Single-line comments
            (r'#.*', style_comment),             # Single-line comments
            (r'"(?:\\.|[^"\\])*"', style_string),# Strings
            (r'@\w+', style_annotation),         # Annotations
            (r'\b(?:if|else|for|String|return|true|false|then|end if|break|boolean|given|send)\b', style_keyword), # Selected keywords
        ]

        while javaCode:
            match_obj = None
            match_start = len(javaCode)
            match_end = len(javaCode)
            match_style = style_normal

            # Find earliest match
            for pattern, style in patterns:
                m = re.search(pattern, javaCode)
                if m and m.start() < match_start:
                    match_obj = m
                    match_start = m.start()
                    match_end = m.end()
                    match_style = style

            if match_obj:
                # Insert text before match (normal style)
                if match_start > 0:
                    doc.insertString(doc.getLength(), javaCode[:match_start], style_normal)

                # Insert matched text (styled)
                doc.insertString(doc.getLength(), javaCode[match_start:match_end], match_style)

                # Move past matched text
                javaCode = javaCode[match_end:]
            else:
                # No more matches, insert rest as normal
                doc.insertString(doc.getLength(), javaCode, style_normal)
                break

        # Scroll to top after inserting text
        if processWhat == "Bambdas":
            self._tbBambdasScript.setCaretPosition(0)
        elif processWhat == "Dict":
            self._tabDictResultDisplay.setCaretPosition(0)


    def funcBambdasUIReset(self, ev=None):
        self._lblBambdasNotification2.setForeground (Color.black)
        self._lblBambdasNotification2.text = "Click 'Run' to generate Bambdas Script!"
        self._cbBambdasColorScope.setSelectedIndex(7)
        self._cbBambdasforWhat.setSelectedIndex(0)
        self._cbBambdasColorScopeSecondary.setSelectedIndex(9)
        self._cbBambdasColorKeyWords.setSelectedIndex(0)
        self._cbBambdasDisplayDays.setSelectedIndex(5)
        self._cbBambdasProcessDays.setSelectedIndex(5)
        self._tbBambdasScopeURLs.setText(self._txBambdasScopeURLs)
        self._tbBambdasScopeDoneURLs.setText(self._txBambdasScopeDoneURLs)
        self._tbBambdasBlackListedURLs.setText(self._txBambdasBlackListedURLs)
        self._tbBambdasScopeURLs.setForeground(Color.GRAY)
        self._tbBambdasScopeDoneURLs.setForeground(Color.GRAY)
        self._tbBambdasBlackListedURLs.setForeground(Color.GRAY)
        self.updateBambdasScriptText("/* Bambdas Script will be in here automatically */")
        self._cbBambdasScope.setSelected(False)
        self._rbBambdasScopeHideShow.setSelected(True)
        self._rbBambdasScopeHideShow.setEnabled(False)
        self._rbBambdasScopeHighlight.setSelected(False)
        self._rbBambdasScopeHighlight.setEnabled(False)
        self._cbBambdasColorInScope.setSelectedIndex(0)
        self._cbBambdasColorInScope.setEnabled(False)
        self._cbBambdasExtIgnore.setSelected(True)
        self._cbBambdasDisplayDays.setEnabled(True)
        self._cbBambdasProcessDays.setEnabled(True)
        self._cbBambdasSearchinReq.setSelected(False)
        self._cbBambdasSearchinRes.setSelected(False)
        self._cbBambdasSearchinURL.setSelected(False)
        
        self._cbBambdasSearchHTMLComments.setSelected(False)
        
        self._txtBambdasExtIgnoreKeywords.text = "js, gif, jpg, png, svg, css, ico, woff, woff2"
        self._txtBambdasExtIgnoreKeywords.setEnabled(True)
        self._cbBambdasExtIgnore.setSelected(True)

        self._txtBambdasHTTPMethods.text = "HEAD, OPTIONS"
        self._txtBambdasHTTPMethods.setEnabled(True)
        self._cbBambdasHTTPMethods.setSelected(True)
        
        self._txtBambdasValuable.text = "debug, admin, config, secret, token, password, hash, credential"
        self._txtBambdasValuable.setEnabled(False)
        self._cbBambdasValuable.setSelected(False)

        self._txtBambdasFilesDownloadable.text = "back, backup, bak, bin, cache, conf, config, csv, doc, docx, gz, inc, ini, jar, log, old, pdf, ppt, pptx, rar, readme, tar, txt, xls, xlsx, zip, 7z"
        self._txtBambdasFilesDownloadable.setEnabled(False)
        self._cbBambdasFilesDownloadable.setSelected(False)

        self._txtBambdasSQLiKeywords.text = "category, id, item, message, name, news, page, password, q, query, report, s, search, thread, user, username, view"
        self._txtBambdasSQLiKeywords.setEnabled(False)
        self._cbBambdasSQLi.setSelected(False)

        self._txtBambdasXSSKeywords.text = "comment, content, description, id, key, keyword, keywords, l, lang, message, name, p, page, q, query, s, search, username"
        self._txtBambdasXSSKeywords.setEnabled(False)
        self._cbBambdasXSS.setSelected(False)

        self._txtBambdasLFIKeywords.text = "conf, content, detail, dir, doc, document, download, file, folder, inc, include, locate, page, path, show, template, url, view, read, load"
        self._txtBambdasLFIKeywords.setEnabled(False)
        self._cbBambdasLFI.setSelected(False)

        self._txtBambdasSSRFKeywords.text = "callback, dest, destination, host, next, out, path, redirect, return, site, target, to, uri, url, view"
        self._txtBambdasSSRFKeywords.setEnabled(False)
        self._cbBambdasSSRF.setSelected(False)

        self._txtBambdasORedKeywords.text = "dest, destination, go, next, out, redir, redirect, redirect_uri, redirect_url, return, return_path, return_to, returnTo, returnUrl, target, to, uri, url"
        self._txtBambdasORedKeywords.setEnabled(False)
        self._cbBambdasORed.setSelected(False)

        self._txtBambdasRCEKeywords.text = "arg, cmd, code, command, exe, exec, execute, ping, print, process, run"
        self._txtBambdasRCEKeywords.setEnabled(False)
        self._cbBambdasRCE.setSelected(False)

        self._txtBambdasVulnJSKeywords.text = "eval(, setTimeout(, setInterval(, document.write(, innerHTML, document.createElement(, document.execCommand(, document.domain, window.location.href, document.cookie, document.URL, document.referrer, window.open(, document.body.innerHTML, element.setAttribute(, element.outerHTML, XMLHttpRequest(, fetch(, navigator.sendBeacon("
        self._txtBambdasVulnJSKeywords.setEnabled(False)
        self._cbBambdasVulnJS.setSelected(False)

        self._cbBambdasSearchinReqFunc()
        self._cbBambdasSearchinResFunc()
        self._cbBambdasSearchinURLFunc()
        return


    def _tabBambdasUI(self):
        self._btnBambdasRun = JButton("               Run              ", actionPerformed=self.funcBambdasRun)
        self._btnBambdasRun.setToolTipText("Generate the Bambdas script based on the options below.")
        self._btnBambdasReset = JButton("               Reset              ", actionPerformed=self.funcBambdasUIReset)
        self._btnBambdasReset.setToolTipText("Clear all fields and restore default settings.")

        self._lblBambdasforWhat = JLabel("Bambdas script target")
        self._lblBambdasforWhat.setVisible(False)
        self._lblBambdasforWhat.setToolTipText("Select what this Bambdas script will operate on.")
        self._cbBambdasforWhat = JComboBox(('View filter - HTTP history', 'Capture Filter'))
        self._cbBambdasforWhat.setEnabled(False)
        
        self._lblBambdasScope = JLabel("Only process in-scope items")
        self._cbBambdasScope = JCheckBox('', False, itemStateChanged=self._cbBambdasScopeFunc)
        self._lblBambdasScope.setToolTipText("Choose whether to show only items within the current project scope or all items.")
        self._cbBambdasScope.setToolTipText("Toggle to show only in-scope items or everything.")

        # Radio buttons – mode selector for the scope checkbox
        self._rbBambdasScopeHideShow = JRadioButton("Hide/Show", True, actionPerformed=self._rbBambdasScopeFunc)
        self._rbBambdasScopeHideShow.setToolTipText("Filter out items that are not in scope (default behaviour).")
        self._rbBambdasScopeHideShow.setEnabled(False)
        self._rbBambdasScopeHighlight = JRadioButton("Highlight", False, actionPerformed=self._rbBambdasScopeFunc)
        self._rbBambdasScopeHighlight.setToolTipText("Keep all items visible but highlight the ones that are in scope.")
        self._rbBambdasScopeHighlight.setEnabled(False)
        self._bgBambdasScope = ButtonGroup()
        self._bgBambdasScope.add(self._rbBambdasScopeHideShow)
        self._bgBambdasScope.add(self._rbBambdasScopeHighlight)

        # Color selector for Burp-scope items (Highlight mode only)
        self._lblBambdasColorInScope = JLabel("Color for in-scope items")
        self._cbBambdasColorInScope = JComboBox(('NONE', 'BLUE', 'CYAN', 'GRAY', 'GREEN', 'MAGENTA', 'ORANGE', 'PINK', 'RED', 'YELLOW'))
        self._cbBambdasColorInScope.setSelectedIndex(0)
        self._cbBambdasColorInScope.setEnabled(False)
        self._lblBambdasColorInScope.setToolTipText("Highlight color applied to items that match the Burp Suite project scope (Highlight mode only).")
        self._cbBambdasColorInScope.setToolTipText("Highlight color applied to items that match the Burp Suite project scope (Highlight mode only).")
        
        self._txtBambdasSearchHTMLCommnets = JTextField("The search will occur between the '<!--' and '-->' tags.", 100)
        self._txtBambdasSearchHTMLCommnets.setEnabled(False)
        self._cbBambdasSearchHTMLComments = JCheckBox('Search HTML comments', False)
        self._txtBambdasSearchHTMLCommnets.setToolTipText("Search HTML comments")
        self._cbBambdasSearchHTMLComments.setToolTipText("Search HTML comments")

        self._lblBambdasNotification1 = JLabel(" ")
        self._lblBambdasNotification2 = JLabel("Click 'Run' to generate Bambdas Script!")

        self._lblBambdasColorScope = JLabel("Color for testing scope")
        self._cbBambdasColorScope = JComboBox(('NONE', 'BLUE', 'CYAN', 'GRAY', 'GREEN', 'MAGENTA', 'ORANGE', 'PINK', 'RED', 'YELLOW'))
        self._lblBambdasColorScope.setToolTipText("Select the highlight color for testing scope.")
        self._cbBambdasColorScope.setToolTipText("Select the highlight color for testing scope.")
        
        self._lblBambdasColorScopeSecondary = JLabel("Color for tested URLs")
        self._cbBambdasColorScopeSecondary = JComboBox(('NONE', 'BLUE', 'CYAN', 'GRAY', 'GREEN', 'MAGENTA', 'ORANGE', 'PINK', 'RED', 'YELLOW'))
        self._cbBambdasColorScopeSecondary.setToolTipText("Select the highlight color for tested endpoints")
        self._lblBambdasColorScopeSecondary.setToolTipText("Select the highlight color for tested endpoints")

        self._lblBambdasColorKeyWords = JLabel("Color for parameters/keywords")
        self._cbBambdasColorKeyWords = JComboBox(('NONE', 'BLUE', 'CYAN', 'GRAY', 'GREEN', 'MAGENTA', 'ORANGE', 'PINK', 'RED', 'YELLOW'))
        self._lblBambdasColorKeyWords.setToolTipText("Select the highlight color when parameters or keywords match.")
        self._cbBambdasColorKeyWords.setToolTipText("Select the highlight color when parameters or keywords match.")
    
        self._lblBambdasSearchScope = JLabel("Keyword search location")
        self._lblBambdasSearchScope.setToolTipText("Choose where keywords should be searched.")
        self._cbBambdasSearchinURL = JCheckBox('in URL', False, itemStateChanged=self._cbBambdasSearchinURLFunc)
        self._cbBambdasSearchinURL.setToolTipText("Search for keywords in URLs.")
        self._cbBambdasSearchinReq = JCheckBox('in Requests', False, itemStateChanged=self._cbBambdasSearchinReqFunc)
        self._cbBambdasSearchinReq.setToolTipText("Search for keywords in requests.")
        self._cbBambdasSearchinRes = JCheckBox('in Responses', False, itemStateChanged=self._cbBambdasSearchinResFunc)
        self._cbBambdasSearchinRes.setToolTipText("Search for keywords in responses.")

        self._lblBambdasDisplayDays = JLabel("Display window (days)")
        self._cbBambdasDisplayDays = JComboBox(('1 Day', '2 Days', '3 Days', '7 Days', '14 Days', '30 Days', '365 Days'))
        self._lblBambdasDisplayDays.setToolTipText("How many past days of data to display.")
        self._cbBambdasDisplayDays.setToolTipText("How many past days of data to display.")
        self._lblBambdasProcessDays = JLabel("Processing window (days)")
        self._cbBambdasProcessDays = JComboBox(('1 Day', '2 Days', '3 Days', '7 Days', '14 Days', '30 Days', '365 Days'))
        self._lblBambdasProcessDays.setToolTipText("How many past days of data to process.")
        self._cbBambdasProcessDays.setToolTipText("How many past days of data to process.")

        self._cbBambdasHTTPMethods = JCheckBox('HTTP methods to ignore.', True, itemStateChanged=self._cbBambdasHTTPMethodsFunc)
        self._txtBambdasHTTPMethods = JTextField("", 100)
        self._txtBambdasHTTPMethods.setToolTipText("Enter HTTP methods to exclude (comma-separated).")
        self._cbBambdasHTTPMethods.setToolTipText("List HTTP methods to exclude from processing (e.g., HEAD, OPTIONS).")

        self._cbBambdasValuable = JCheckBox('Valuable keywords', False, itemStateChanged=self._cbBambdasValuableFunc)
        self._txtBambdasValuable = JTextField("", 100)
        self._txtBambdasValuable.setToolTipText("Keywords that mark as important (comma-separated).")
        self._cbBambdasValuable.setToolTipText("Flag items containing high-value keywords.")
        
        self._cbBambdasFilesDownloadable = JCheckBox('Downloadable file extensions', False, itemStateChanged=self._cbBambdasFilesDownFunc)
        self._txtBambdasFilesDownloadable = JTextField("", 100)
        self._txtBambdasFilesDownloadable.setToolTipText("Mark items with these extensions as suspicious, potentially downloadable (comma-separated).")
        self._cbBambdasFilesDownloadable.setToolTipText("Flag responses containing files suspected to be downloadable")

        self._cbBambdasSQLi = JCheckBox('SQLi-suspect identifiers', False, itemStateChanged=self._cbBambdasSQLiFunc)
        self._txtBambdasSQLiKeywords = JTextField("", 100)
        self._txtBambdasSQLiKeywords.setToolTipText("Keywords/parameter names that may indicate SQL injection (comma-separated).")
        self._cbBambdasSQLi.setToolTipText("Flag items containing potential SQLi indicators.")
        
        self._cbBambdasXSS = JCheckBox('XXS-suspect identifiers', False, itemStateChanged=self._cbBambdasXSSFunc)
        self._txtBambdasXSSKeywords = JTextField("", 100)
        self._txtBambdasXSSKeywords.setToolTipText("Keywords/parameter names that may indicate XSS injection (comma-separated).")
        self._cbBambdasXSS.setToolTipText("Flag items containing potential XSS indicators.")
        
        self._cbBambdasLFI = JCheckBox('LFI-suspect identifiers', False, itemStateChanged=self._cbBambdasLFIFunc)
        self._txtBambdasLFIKeywords = JTextField("", 100)
        self._txtBambdasLFIKeywords.setToolTipText("Keywords/parameter names that may indicate LFI injection (comma-separated).")
        self._cbBambdasLFI.setToolTipText("Flag items containing potential LFI indicators.")
    
        self._cbBambdasSSRF = JCheckBox('SSRF-suspect identifiers', False, itemStateChanged=self._cbBambdasSSRFFunc)
        self._txtBambdasSSRFKeywords = JTextField("", 100)
        self._txtBambdasSSRFKeywords.setToolTipText("Keywords/parameter names that may indicate SSRF injection (comma-separated).")
        self._cbBambdasSSRF.setToolTipText("Flag items containing potential SSRF indicators.")
    
        self._cbBambdasORed = JCheckBox('Open Redirect-suspect identifiers', False, itemStateChanged=self._cbBambdasORedFunc)
        self._txtBambdasORedKeywords = JTextField("", 100)
        self._txtBambdasORedKeywords.setToolTipText("Keywords/parameter names that may indicate Open Redirect injection (comma-separated).")
        self._cbBambdasORed.setToolTipText("Flag items containing potential Open Redirect indicators.")
    
        self._cbBambdasRCE = JCheckBox('RCE-suspect identifiers', False, itemStateChanged=self._cbBambdasRCEFunc)
        self._txtBambdasRCEKeywords = JTextField("", 100)
        self._txtBambdasRCEKeywords.setToolTipText("Keywords/parameter names that may indicate RCE injection (comma-separated).")
        self._cbBambdasRCE.setToolTipText("Flag items containing potential RCE indicators.")
    
        self._cbBambdasVulnJS = JCheckBox('Vulnerable JS Functions', False, itemStateChanged=self._cbBambdasVulnJSFunc)
        self._txtBambdasVulnJSKeywords = JTextField("", 100)
        self._txtBambdasVulnJSKeywords.setToolTipText("Potentially risky JavaScript functions to look for (comma-separated).")
        self._cbBambdasVulnJS.setToolTipText("Flag responses containing potentially risky JavaScript functions.")
    
        self._cbBambdasExtIgnore = JCheckBox('File extensions to ignore', True, itemStateChanged=self._cbBambdasExtIgnoreFunc)
        self._txtBambdasExtIgnoreKeywords = JTextField("", 100)
        self._txtBambdasExtIgnoreKeywords.setToolTipText("File extensions to exclude from processing (comma-separated).")
        self._cbBambdasExtIgnore.setToolTipText("Exclude items with these file extensions.")

        __tabBambdasPanelTop_Left = JPanel()
        layout = GroupLayout(__tabBambdasPanelTop_Left)
        __tabBambdasPanelTop_Left.setLayout(layout)
        layout.setAutoCreateGaps(True)
        layout.setAutoCreateContainerGaps(True)
    
        layout.setHorizontalGroup(
            layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                    .addComponent(self._btnBambdasRun)
                    .addComponent(self._lblBambdasforWhat)
                    .addComponent(self._lblBambdasScope)
                    .addComponent(self._lblBambdasColorInScope)
                    .addComponent(self._cbBambdasExtIgnore)
                    .addComponent(self._lblBambdasColorScope)
                    .addComponent(self._lblBambdasColorScopeSecondary)
                    .addComponent(self._lblBambdasColorKeyWords)
                    .addComponent(self._lblBambdasDisplayDays)
                    .addComponent(self._lblBambdasProcessDays)
                    .addComponent(self._lblBambdasSearchScope)
                    .addComponent(self._cbBambdasHTTPMethods)
                    .addComponent(self._cbBambdasSearchHTMLComments)
                    .addComponent(self._cbBambdasFilesDownloadable)
                    .addComponent(self._cbBambdasVulnJS)
                    .addComponent(self._cbBambdasValuable)
                    .addComponent(self._cbBambdasSQLi)
                    .addComponent(self._cbBambdasXSS)
                    .addComponent(self._cbBambdasLFI)
                    .addComponent(self._cbBambdasSSRF)
                    .addComponent(self._cbBambdasORed)
                    .addComponent(self._cbBambdasRCE)
                    .addComponent(self._cbBambdasExtIgnore)
                    .addComponent(self._lblBambdasNotification1))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                    .addComponent(self._btnBambdasReset)
                    .addComponent(self._cbBambdasforWhat, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(self._cbBambdasScope)
                        .addGap(10)
                        .addComponent(self._rbBambdasScopeHideShow)
                        .addGap(6)
                        .addComponent(self._rbBambdasScopeHighlight))
                    .addComponent(self._cbBambdasColorInScope, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addComponent(self._txtBambdasExtIgnoreKeywords)
                    .addComponent(self._cbBambdasColorScope, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addComponent(self._cbBambdasColorScopeSecondary, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addComponent(self._cbBambdasColorKeyWords, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addComponent(self._cbBambdasDisplayDays, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addComponent(self._cbBambdasProcessDays, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(self._cbBambdasSearchinURL)
                        .addGap(10)
                        .addComponent(self._cbBambdasSearchinReq)
                        .addGap(10)
                        .addComponent(self._cbBambdasSearchinRes))
                    .addComponent(self._txtBambdasHTTPMethods)
                    .addComponent(self._txtBambdasSearchHTMLCommnets)
                    .addComponent(self._txtBambdasFilesDownloadable)
                    .addComponent(self._txtBambdasVulnJSKeywords)
                    .addComponent(self._txtBambdasValuable)
                    .addComponent(self._txtBambdasSQLiKeywords)
                    .addComponent(self._txtBambdasXSSKeywords)
                    .addComponent(self._txtBambdasLFIKeywords)
                    .addComponent(self._txtBambdasSSRFKeywords)
                    .addComponent(self._txtBambdasORedKeywords)
                    .addComponent(self._txtBambdasRCEKeywords)
                    .addComponent(self._lblBambdasNotification2))
        )
    
        layout.setVerticalGroup(
            layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._btnBambdasRun)
                    .addComponent(self._btnBambdasReset))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasforWhat)
                    .addComponent(self._cbBambdasforWhat))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasScope)
                    .addComponent(self._cbBambdasScope)
                    .addComponent(self._rbBambdasScopeHideShow)
                    .addComponent(self._rbBambdasScopeHighlight))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasColorInScope)
                    .addComponent(self._cbBambdasColorInScope))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasExtIgnore)
                    .addComponent(self._txtBambdasExtIgnoreKeywords))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasColorScope)
                    .addComponent(self._cbBambdasColorScope))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasColorScopeSecondary)
                    .addComponent(self._cbBambdasColorScopeSecondary))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasColorKeyWords)
                    .addComponent(self._cbBambdasColorKeyWords))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasDisplayDays)
                    .addComponent(self._cbBambdasDisplayDays))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasProcessDays)
                    .addComponent(self._cbBambdasProcessDays))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasSearchScope)
                    .addComponent(self._cbBambdasSearchinURL)
                    .addComponent(self._cbBambdasSearchinReq)
                    .addComponent(self._cbBambdasSearchinRes))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasHTTPMethods)
                    .addComponent(self._txtBambdasHTTPMethods))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasSearchHTMLComments)
                    .addComponent(self._txtBambdasSearchHTMLCommnets))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasFilesDownloadable)
                    .addComponent(self._txtBambdasFilesDownloadable))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasVulnJS)
                    .addComponent(self._txtBambdasVulnJSKeywords))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasValuable)
                    .addComponent(self._txtBambdasValuable))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasSQLi)
                    .addComponent(self._txtBambdasSQLiKeywords))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasXSS)
                    .addComponent(self._txtBambdasXSSKeywords))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasLFI)
                    .addComponent(self._txtBambdasLFIKeywords))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasSSRF)
                    .addComponent(self._txtBambdasSSRFKeywords))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasORed)
                    .addComponent(self._txtBambdasORedKeywords))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._cbBambdasRCE)
                    .addComponent(self._txtBambdasRCEKeywords))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self._lblBambdasNotification1)
                    .addComponent(self._lblBambdasNotification2))
        )

        self._tbBambdasScopeURLs = JTextPane()
        self._tbBambdasScopeURLs.setToolTipText("Define test scope: one URL per line. Leave blank to include everything, and * acts like a regex wildcard.")
        self._txBambdasScopeURLs = "URLs in testing scope. Wildcard * matches any characters. Examples:\n        > /\n                Include all paths\n        > /api/users\n                Include exact match only\n                + /api/users\n                - /api/users/, /api/users/profile\n        > /api/users*\n                Include everything beneath\n                + /api/users/profile, /api/users/anything/more/path\n        # Use hash for comments"
        placeholderText1 = self._txBambdasScopeURLs
        self._tbBambdasScopeURLs.setText(placeholderText1)
        self._tbBambdasScopeURLs.setForeground(Color.GRAY)
        listener1 = MyFocusListener(self._tbBambdasScopeURLs, placeholderText1)
        self._tbBambdasScopeURLs.addFocusListener(listener1)

        self._lbBambdasScopeURLs = JLabel("Definition of testing scope", SwingConstants.LEFT)
        self._lbBambdasScopeURLs.setFont(self._lbBambdasScopeURLs.getFont().deriveFont(Font.BOLD))

        self._tbBambdasScopeDoneURLs = JTextPane()
        self._tbBambdasScopeDoneURLs.setToolTipText("Mark already-tested endpoints: one URL per line. Leave blank if none, and * acts like a regex wildcard.")
        self._txBambdasScopeDoneURLs = "Already tested URLs. Wildcard * matches any characters. Examples:\n        > /api/*/users/*/profile\n                Asterisk matches any segment (IDs, paths, strings)\n                + /api/v1/users/dashboard/1337/profile\n                - /api/v1/users/dashboard/profile/settings\n        > /api/*/users/*/profile*\n                Trailing * includes remaining paths\n                + /api/v1/users/portal/1/profile/settings\n        # Use hash for comments"
        placeholderText2 = self._txBambdasScopeDoneURLs
        self._tbBambdasScopeDoneURLs.setText(placeholderText2)
        self._tbBambdasScopeDoneURLs.setForeground(Color.GRAY)
        listener2 = MyFocusListener(self._tbBambdasScopeDoneURLs, placeholderText2)
        self._tbBambdasScopeDoneURLs.addFocusListener(listener2)

        self._lbBambdasScopeDoneURLs = JLabel("Already Tested URLs", SwingConstants.LEFT)
        self._lbBambdasScopeDoneURLs.setFont(self._lbBambdasScopeDoneURLs.getFont().deriveFont(Font.BOLD))

        self._tbBambdasBlackListedURLs = JTextPane()
        self._tbBambdasBlackListedURLs.setToolTipText("Hide from the history: one URL per line. Leave blank to exclude nothing. Adding '/' will hide everything unless a criteria matches, and * acts like a regex wildcard.")
        self._txBambdasBlackListedURLs = "URLs to hide from HTTP history. Wildcard * matches any characters. Examples:\n        > /metrics/\n                Exact path match\n                + /metrics/\n                - /metrics, /metrics/health\n        > /metrics/*\n                Path and all continuations\n                + /metrics/, /metrics/health\n                - /metrics\n        > /\n                Adding / will hide everything unless other criteria match"
        placeholderText3 = self._txBambdasBlackListedURLs
        self._tbBambdasBlackListedURLs.setText(placeholderText3)
        self._tbBambdasBlackListedURLs.setForeground(Color.GRAY)
        listener3 = MyFocusListener(self._tbBambdasBlackListedURLs, placeholderText3)
        self._tbBambdasBlackListedURLs.addFocusListener(listener3)

        self._lbBambdasBlackListedURLs = JLabel("Black-Listed URLs", SwingConstants.LEFT)
        self._lbBambdasBlackListedURLs.setFont(self._lbBambdasBlackListedURLs.getFont().deriveFont(Font.BOLD))

        __tabBambdasPanelTop_Right = JPanel()
        __tabBambdasPanelTop_Right.setLayout(BoxLayout(__tabBambdasPanelTop_Right, BoxLayout.Y_AXIS))

        __tabBambdasPanelTop_Right.add(self._lbBambdasScopeURLs)
        scrollBambdasScopeURLs = JScrollPane(self._tbBambdasScopeURLs)
        scrollBambdasScopeURLs.setPreferredSize(Dimension(400, 100))
        __tabBambdasPanelTop_Right.add(scrollBambdasScopeURLs)

        __tabBambdasPanelTop_Right.add(self._lbBambdasScopeDoneURLs)
        scrollBambdasScopeDoneURLs = JScrollPane(self._tbBambdasScopeDoneURLs)
        scrollBambdasScopeDoneURLs.setPreferredSize(Dimension(400, 100))
        __tabBambdasPanelTop_Right.add(scrollBambdasScopeDoneURLs)

        __tabBambdasPanelTop_Right.add(self._lbBambdasBlackListedURLs)
        scrollBambdasBlackListedURLs = JScrollPane(self._tbBambdasBlackListedURLs)
        scrollBambdasBlackListedURLs.setPreferredSize(Dimension(400, 100))
        __tabBambdasPanelTop_Right.add(scrollBambdasBlackListedURLs)

        _tabBambdasPanelTop = JSplitPane(JSplitPane.HORIZONTAL_SPLIT)
 
        _tabBambdasPanelTop.setResizeWeight(0.5)
        _tabBambdasPanelTop.setLeftComponent(__tabBambdasPanelTop_Left)
        _tabBambdasPanelTop.setRightComponent(__tabBambdasPanelTop_Right)
        _tabBambdasPanelBottom = JPanel(BorderLayout())
        self._tbBambdasScript = JTextPane()
        self._tbBambdasScript.setContentType("text")
        self._tbBambdasScript.setEditable(False)
        self._tbBambdasScript.setToolTipText("The generated Bambdas script will appear here after you click Run.")
        self.updateBambdasScriptText("/* Bambdas Script will be in here automatically */")
        scroll_pane = JScrollPane(self._tbBambdasScript)

        # Add custom MouseWheelListener to slow down scrolling
        class SlowScrollMouseWheelListener(MouseWheelListener):
            def mouseWheelMoved(inner_self, e):
                scrollBar = scroll_pane.getVerticalScrollBar()
                amount = e.getUnitsToScroll() * 5  # Adjust for scroll speed
                scrollBar.setValue(scrollBar.getValue() + amount)
                e.consume()  # Prevent default fast scroll

        self._tbBambdasScript.addMouseWheelListener(SlowScrollMouseWheelListener())

        _tabBambdasPanelBottom.add(scroll_pane, BorderLayout.CENTER)
        self._tabBambdasPanel = JSplitPane(JSplitPane.VERTICAL_SPLIT)
        self._tabBambdasPanel.setResizeWeight(0.1)
        self._tabBambdasPanel.setBorder(EmptyBorder(10, 10, 10, 10))
        self._tabBambdasPanel.setTopComponent(_tabBambdasPanelTop)
        self._tabBambdasPanel.setBottomComponent(_tabBambdasPanelBottom)

        self.funcBambdasUIReset()
        return


class MyFocusListener(FocusListener):
    def __init__(self, textPane, placeholder):
        self.textPane = textPane
        self.placeholder = placeholder

    def focusGained(self, event):
        if self.textPane.getText() == self.placeholder:
            self.textPane.setText("")
            self.textPane.setForeground(Color.BLACK)

    def focusLost(self, event):
        if self.textPane.getText().strip() == "":
            self.textPane.setText(self.placeholder)
            self.textPane.setForeground(Color.GRAY)
