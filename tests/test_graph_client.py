import pytest
from unittest.mock import AsyncMock, patch
from graph_auth_delegated import PersonalGraphClient

@pytest.mark.asyncio
async def test_get_my_profile():
    with patch('graph_auth_delegated.DeviceCodeCredential'):
        client = PersonalGraphClient()
        
        # Mock Graph API response
        mock_me = AsyncMock()
        mock_me.display_name = "Test User"
        
        with patch.object(client.graph_client.me, 'get', return_value=mock_me):
            result = await client.get_my_profile()
            assert result.display_name == "Test User"

@pytest.mark.asyncio
async def test_list_onedrive_files():
    with patch('graph_auth_delegated.DeviceCodeCredential'):
        client = PersonalGraphClient()
        
        # Test file listing
        mock_files = AsyncMock()
        mock_files.value = []
        
        with patch.object(client.graph_client.me.drive.root.children, 'get', return_value=mock_files):
            await client.list_onedrive_files()
            # Should not raise exception
