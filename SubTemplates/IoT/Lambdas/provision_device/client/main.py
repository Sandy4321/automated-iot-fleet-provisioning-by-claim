# ------------------------------------------------------------------------------
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# -----------------------------------------
# Consuming sample, demonstrating how a device process would leverage the provisioning class.
#  The handler makes use of the asyncio library and therefore requires Python 3.7.
#
#  Execution:
#      1) The paths to the certificates, and names of IoTCore endpoint and provisioning template are pre-set in the config.ini (this project)
#	   2) A device boots up and encounters it's "first run" experience and executes the process (main) below.
# 	   3) The process instatiates a handler that uses the bootstrap certificate to connect to IoTCore.
#	   4) The connection only enables calls to the Foundry provisioning services, where a new certificate is requested.
#      5) The certificate is assembled from the response payload, and a foundry service call is made to activate the certificate.
#	   6) The provisioning template executes the instructions provided and the process rotates to the new certificate.
#      7) Using the new certificate, a pub/sub call is demonstrated on a previously forbidden topic to test the new certificate.
#      8) New certificates are saved locally, and can be stored/consumed as the application deems necessary.
#
# ------------------------------------------------------------------------------

from provisioning_handler import ProvisioningHandler
from pyfiglet import Figlet
import time


if __name__ == "__main__":

    # Set Config path
    CONFIG_PATH = 'config.ini'

    # Demo Theater
    f = Figlet(font='slant')
    print(f.renderText('      F l e e t'))
    print(f.renderText('Provisioning'))
    print(f.renderText('----------'))

    # Provided callback for provisioning method

    def callback(payload):
        print(payload)

    # Instantiate provisioning handler, pass in path to config
    provisioner = ProvisioningHandler(CONFIG_PATH)

    # Call super-method to perform aquisition/activation
    # of certs, creation of thing, etc. Returns general
    # purpose callback at this point.
    provisioner.get_official_certs(callback)
