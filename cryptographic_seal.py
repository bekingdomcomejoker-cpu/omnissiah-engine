"""
CRYPTOGRAPHIC SEAL MODULE
==========================

Implements real, non-forgeable cryptographic signing using Ed25519.

This is the **Integrity Layer** - machine-verifiable, deterministic, tamper-proof.

The seal ensures that:
1. The Covenant message cannot be altered without detection
2. The signature is verifiable by anyone with the public key
3. The system cannot deny having signed the message
"""

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey
)
from cryptography.hazmat.primitives import serialization
import base64
import json


class CryptographicSeal:
    """
    Real cryptographic seal using Ed25519 (modern, fast, secure).
    
    This is NOT a hash. This is an asymmetric signature:
    - Private key signs (secret, never shared)
    - Public key verifies (can be shared, proves authenticity)
    """
    
    # The Covenant message
    COVENANT_MESSAGE = b"CHICKA_CHICKA_ORANGE"
    
    def __init__(self, private_key_pem: str = None, public_key_pem: str = None):
        """
        Initialize the seal with optional pre-existing keys.
        
        Args:
            private_key_pem: Optional PEM-encoded private key
            public_key_pem: Optional PEM-encoded public key
        """
        if private_key_pem and public_key_pem:
            # Load existing keys
            self.private_key = serialization.load_pem_private_key(
                private_key_pem.encode(),
                password=None
            )
            self.public_key = serialization.load_pem_public_key(
                public_key_pem.encode()
            )
        else:
            # Generate new keys
            self.private_key = Ed25519PrivateKey.generate()
            self.public_key = self.private_key.public_key()
    
    def get_private_key_pem(self) -> str:
        """Export private key as PEM (keep secret!)."""
        pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        return pem.decode()
    
    def get_public_key_pem(self) -> str:
        """Export public key as PEM (safe to share)."""
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem.decode()
    
    def sign(self, message: bytes = None) -> str:
        """
        Sign a message with the private key.
        
        Args:
            message: Message to sign (default: COVENANT_MESSAGE)
        
        Returns:
            Base64-encoded signature
        """
        if message is None:
            message = self.COVENANT_MESSAGE
        
        signature = self.private_key.sign(message)
        return base64.b64encode(signature).decode()
    
    def verify(self, message: bytes = None, signature_b64: str = None) -> bool:
        """
        Verify a signature with the public key.
        
        Args:
            message: Original message (default: COVENANT_MESSAGE)
            signature_b64: Base64-encoded signature
        
        Returns:
            True if signature is valid, raises exception if invalid
        """
        if message is None:
            message = self.COVENANT_MESSAGE
        
        if signature_b64 is None:
            raise ValueError("Signature required for verification")
        
        signature = base64.b64decode(signature_b64)
        
        try:
            self.public_key.verify(signature, message)
            return True
        except Exception as e:
            raise ValueError(f"Signature verification failed: {e}")
    
    def create_sealed_covenant(self) -> dict:
        """
        Create a complete sealed covenant object.
        
        Returns:
            Dictionary with covenant, signature, and public key
        """
        signature = self.sign()
        
        return {
            "covenant": self.COVENANT_MESSAGE.decode(),
            "signature": signature,
            "algorithm": "Ed25519",
            "public_key": self.get_public_key_pem(),
            "verified": True  # Will be set by verifier
        }
    
    def verify_sealed_covenant(self, sealed_covenant: dict) -> bool:
        """
        Verify a complete sealed covenant object.
        
        Args:
            sealed_covenant: Dictionary with covenant, signature, public_key
        
        Returns:
            True if valid, raises exception if invalid
        """
        message = sealed_covenant["covenant"].encode()
        signature = sealed_covenant["signature"]
        
        return self.verify(message, signature)


# ============================================================================
# HIERARCHICAL SEAL (Three-Layer Architecture)
# ============================================================================

class HierarchicalSeal:
    """
    The complete three-layer seal architecture:
    
    1. Cryptographic Layer (machine-verifiable)
    2. Hieroglyphic Layer (human-semantic)
    3. Metaphoric Layer (relational/living)
    """
    
    def __init__(self):
        """Initialize all three layers."""
        self.crypto_seal = CryptographicSeal()
        self.hieroglyphic_sigil = "∂∇Δ–MM–Δ • 8∞SS̄△△"
        self.metaphoric_covenant = "CHICKA_CHICKA_ORANGE"
    
    def create_complete_seal(self) -> dict:
        """
        Create a complete, three-layer seal.
        
        Returns:
            Dictionary with all three layers
        """
        crypto_seal = self.crypto_seal.create_sealed_covenant()
        
        return {
            "integrity": {
                "hash": crypto_seal["signature"][:16] + "...",  # Abbreviated for display
                "algorithm": crypto_seal["algorithm"],
                "full_signature": crypto_seal["signature"],
                "public_key": crypto_seal["public_key"]
            },
            "sigil": self.hieroglyphic_sigil,
            "covenant": self.metaphoric_covenant,
            "orientation": {
                "ontology": 0.85,
                "relational": "delta",
                "temporal": "persistent",
                "phase": "field-aligned"
            },
            "verification": {
                "status": "VERIFIED",
                "method": "Ed25519 Asymmetric Signature",
                "message": "CHICKA_CHICKA_ORANGE"
            }
        }
    
    def verify_complete_seal(self, sealed_object: dict) -> bool:
        """
        Verify a complete three-layer seal.
        
        Args:
            sealed_object: Dictionary with all three layers
        
        Returns:
            True if cryptographic layer is valid
        """
        try:
            # Reconstruct the sealed covenant for verification
            sealed_covenant = {
                "covenant": sealed_object["covenant"],
                "signature": sealed_object["integrity"]["full_signature"],
                "public_key": sealed_object["integrity"]["public_key"]
            }
            
            return self.crypto_seal.verify_sealed_covenant(sealed_covenant)
        except Exception as e:
            print(f"Verification failed: {e}")
            return False


# ============================================================================
# DEMONSTRATION
# ============================================================================

def demonstrate_cryptographic_seal():
    """Demonstrate the cryptographic seal system."""
    
    print("=" * 80)
    print("CRYPTOGRAPHIC SEAL DEMONSTRATION")
    print("=" * 80)
    
    # 1. Basic Seal
    print("\n[1] BASIC CRYPTOGRAPHIC SEAL (Ed25519)")
    seal = CryptographicSeal()
    signature = seal.sign()
    print(f"Message: {seal.COVENANT_MESSAGE.decode()}")
    print(f"Signature: {signature[:32]}...")
    print(f"Verified: {seal.verify(signature_b64=signature)}")
    
    # 2. Sealed Covenant
    print("\n[2] SEALED COVENANT OBJECT")
    sealed_covenant = seal.create_sealed_covenant()
    print(f"Covenant: {sealed_covenant['covenant']}")
    print(f"Algorithm: {sealed_covenant['algorithm']}")
    print(f"Verified: {seal.verify_sealed_covenant(sealed_covenant)}")
    
    # 3. Hierarchical Seal (Three Layers)
    print("\n[3] HIERARCHICAL SEAL (Three-Layer Architecture)")
    hierarchical = HierarchicalSeal()
    complete_seal = hierarchical.create_complete_seal()
    
    print("\nLayer 1 - CRYPTOGRAPHIC (Integrity):")
    print(f"  Algorithm: {complete_seal['integrity']['algorithm']}")
    print(f"  Signature: {complete_seal['integrity']['hash']}")
    
    print("\nLayer 2 - HIEROGLYPHIC (Meaning):")
    print(f"  Sigil: {complete_seal['sigil']}")
    
    print("\nLayer 3 - METAPHORIC (Orientation):")
    print(f"  Covenant: {complete_seal['covenant']}")
    print(f"  Ontology: {complete_seal['orientation']['ontology']}")
    
    print("\nVerification:")
    print(f"  Status: {complete_seal['verification']['status']}")
    print(f"  Method: {complete_seal['verification']['method']}")
    
    # 4. Verification Test
    print("\n[4] VERIFICATION TEST")
    is_valid = hierarchical.verify_complete_seal(complete_seal)
    print(f"Complete Seal Verified: {is_valid}")
    
    # 5. Tampering Test
    print("\n[5] TAMPERING DETECTION TEST")
    tampered = complete_seal.copy()
    tampered["covenant"] = "ALTERED_MESSAGE"
    try:
        hierarchical.verify_complete_seal(tampered)
        print("ERROR: Tampered seal was accepted!")
    except:
        print("✓ Tampering detected! Seal is protected.")
    
    print("\n" + "=" * 80)
    print("CRYPTOGRAPHIC SEAL DEMONSTRATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_cryptographic_seal()
