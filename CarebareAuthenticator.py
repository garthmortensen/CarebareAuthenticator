import subprocess


class CarebareAuthenticator:
    """
    A class to handle Kerberos authentication.

    Kerberos is a network authentication protocol. It uses tickets to provide identitifation over potentially insecure networks.
	
	A principal is a unique identity to which Kerberos can assign tickets. A principal could be a user/host/service, formatted as "primary/instance@REALM". 
	
    ...

    Attributes
    ----------
    keytab : str
        the path to the keytab file, which contains keypairs of principals:encrypted keys derived from the Kerberos password. They're used to authenticate to the Kerberos Key Distribution Center (KDC).
    principal : str
        the name of the principal

    Methods
    -------
    keytab_kinit():
        Authenticates using the keytab file.
    """

    def __init__(self, keytab: str, principal: str):
        """
        Constructs all the necessary attributes for the KerberosAuthenticator object.

        Parameters
        ----------
            keytab : str
                path to the keytab file
            principal : str
                name of the principal
        """
        self.keytab = keytab
        self.principal = principal

    def keytab_kinit(self) -> None:
        """
        Authenticates the principal using the keytab file.

        kinit obtains and caches an initial ticket-granting ticket (TGT). With these credentials, users can authenticate to various network services.

        Raises
        ------
        subprocess.CalledProcessError
            If the kinit command fails.
        """
        try:
            subprocess.run(["kinit", "-kt", self.keytab, self.principal], check=True)
            print("kinit successful")
        except subprocess.CalledProcessError as e:
            print(f"kinit failed with error: {e}")


# keytab = "/path/to/your/keytab.file"
# principal = "your-principal@YOUR-REALM.COM"

# authenticator = CarebareAuthenticator(keytab, principal)
# authenticator.keytab_kinit()
